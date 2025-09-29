from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.matcher import match_resume_to_job
from app.schemas import MatchResponse
import PyPDF2
from docx import Document
import os

app = FastAPI(title="Job Description Matcher API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
if os.path.exists("frontend"):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    """Root endpoint - serve the frontend or API info"""
    if os.path.exists("frontend/index.html"):
        return FileResponse("frontend/index.html")
    return {"message": "Job Description Matcher API", "docs": "/docs", "frontend": "Visit /static/index.html"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Job Description Matcher API"}

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

@app.post("/match", response_model=MatchResponse)
async def match_job_resume(
    job_description: str = Form(...),
    resume_text: str = Form(None),
    resume_file: UploadFile = File(None)
):
    try:
        if resume_text:
            resume = resume_text
        elif resume_file:
            if resume_file.filename.endswith(".pdf"):
                resume = extract_text_from_pdf(resume_file.file)
            elif resume_file.filename.endswith(".docx"):
                resume = extract_text_from_docx(resume_file.file)
            else:
                raise HTTPException(status_code=400, detail="Unsupported file type. Only PDF and DOCX are allowed.")
        else:
            raise HTTPException(status_code=400, detail="No resume input provided.")

        score, missing_keywords = match_resume_to_job(resume, job_description)
        return MatchResponse(
            match_score=round(score * 100, 2),
            missing_keywords=missing_keywords
        )
    except Exception as e:
        print(f"Error in /match: {e}")
        raise HTTPException(status_code=500, detail=str(e))
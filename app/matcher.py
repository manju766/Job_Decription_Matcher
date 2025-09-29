from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Expanded skills list (add/remove as needed)
SKILLS = {
    "python", "java", "sql", "c++", "javascript", "html", "css", "git", "docker", "linux",
    "aws", "azure", "react", "nodejs", "machine learning", "deep learning", "nlp",
    "data analysis", "excel", "powerbi", "tableau", "django", "flask", "rest api",
    "mongodb", "mysql", "postgresql", "cloud", "devops", "agile", "scrum", "testing",
    "communication", "leadership", "problem-solving", "teamwork", "pandas", "numpy",
    "scikit-learn", "tensorflow", "keras", "fastapi", "flask", "matplotlib", "seaborn",
    "jupyter", "visualization", "statistics", "data engineering", "etl", "big data",
    "hadoop", "spark", "kubernetes", "microservices", "system design", "oop", "restful",
    "api development", "version control", "shell scripting", "bash", "powershell",
    "networking", "security", "encryption", "cloud computing", "web development",
    "frontend", "backend", "full stack", "mobile development", "android", "ios"
}

def extract_skills_spacy(text):
    """
    Extract skills from text using spaCy and a predefined skills list.
    Matches both single and multi-word skills.
    """
    doc = nlp(text.lower())
    found_skills = set()
    # Check for exact skill matches in text
    text_lower = text.lower()
    for skill in SKILLS:
        if skill in text_lower:
            found_skills.add(skill)
    # Also check for noun chunks and entities
    for chunk in doc.noun_chunks:
        if chunk.text in SKILLS:
            found_skills.add(chunk.text)
    for ent in doc.ents:
        if ent.text in SKILLS:
            found_skills.add(ent.text)
    return found_skills

def match_resume_to_job(resume: str, job_description: str):
    """
    Compute similarity between resume and job description using TF-IDF + Cosine Similarity.
    Returns: (similarity_score, missing_skills)
    """
    # Input validation
    if not isinstance(resume, str) or not isinstance(job_description, str):
        raise ValueError("Inputs must be strings.")
    if not resume.strip():
        raise ValueError("Resume cannot be empty.")
    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    try:
        # Build TF-IDF matrix
        docs = [resume, job_description]
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(docs)

        # Compute similarity
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        # Extract skills using spaCy
        resume_skills = extract_skills_spacy(resume)
        job_skills = extract_skills_spacy(job_description)
        missing_skills = sorted(list(job_skills - resume_skills))

        return similarity, missing_skills
    except Exception as e:
        print(f"Error in match_resume_to_job: {e}")
        raise
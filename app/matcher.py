from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Try to load spaCy, fallback to regex if not available
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except (ImportError, OSError):
    SPACY_AVAILABLE = False

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
    "frontend", "backend", "full stack", "mobile development", "android", "ios",
    "pytorch", "computer vision", "blockchain", "solidity", "smart contracts", "web3",
    "redis", "elasticsearch", "graphql", "typescript", "vue.js", "angular", "next.js",
    "spring boot", "hibernate", "maven", "gradle", "jenkins", "ci/cd", "terraform",
    "ansible", "puppet", "chef", "prometheus", "grafana", "elk stack", "splunk",
    "kafka", "rabbitmq", "apache airflow", "dbt", "snowflake", "databricks", "redshift",
    "bigquery", "gcp", "oracle", "salesforce", "sap", "jira", "confluence", "slack",
    "figma", "adobe creative suite", "photoshop", "illustrator", "ui/ux design", "wireframing",
    "prototyping", "user research", "a/b testing", "seo", "sem", "google analytics"
}

def extract_skills_spacy(text):
    """
    Extract skills from text using spaCy (if available) or regex fallback.
    Matches both single and multi-word skills.
    """
    found_skills = set()
    text_lower = text.lower()
    
    # Basic skill extraction using string matching
    for skill in SKILLS:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)
    
    # If spaCy is available, use it for better extraction
    if SPACY_AVAILABLE:
        try:
            doc = nlp(text_lower)
            for chunk in doc.noun_chunks:
                if chunk.text in SKILLS:
                    found_skills.add(chunk.text)
            for ent in doc.ents:
                if ent.text in SKILLS:
                    found_skills.add(ent.text)
        except:
            pass  # Fallback to regex-only approach
    
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
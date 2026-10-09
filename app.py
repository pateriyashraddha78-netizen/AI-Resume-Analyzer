import re
from io import BytesIO

from flask import Flask, render_template, request
from pypdf import PdfReader

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB

SKILLS = [
    "python", "java", "javascript", "html", "css", "react", "node.js",
    "flask", "django", "sql", "mysql", "postgresql", "mongodb", "git",
    "github", "machine learning", "deep learning", "data analysis",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "aws",
    "azure", "docker", "rest api", "api", "communication", "testing",
    "selenium", "manual testing", "agile", "figma", "bootstrap"
]

def extract_pdf_text(file_storage):
    """Extract text from a PDF uploaded by the user."""
    reader = PdfReader(BytesIO(file_storage.read()))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def find_skills(text):
    normalized = normalize(text)
    found = []
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(found)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        resume = request.files.get("resume")
        job_description = request.form.get("job_description", "").strip()

        if not resume or not resume.filename:
            error = "Please choose a PDF resume."
        elif not resume.filename.lower().endswith(".pdf"):
            error = "Please upload a PDF file."
        elif not job_description:
            error = "Please paste the job description."
        else:
            try:
                resume_text = extract_pdf_text(resume)
                if not resume_text.strip():
                    error = "No selectable text was found. Try a text-based PDF rather than a scanned image."
                else:
                    resume_skills = find_skills(resume_text)
                    required_skills = find_skills(job_description)
                    matched = sorted(set(resume_skills) & set(required_skills))
                    missing = sorted(set(required_skills) - set(resume_skills))
                    score = round((len(matched) / len(set(required_skills))) * 100) if required_skills else 0
                    result = {
                        "score": score,
                        "resume_skills": resume_skills,
                        "required_skills": required_skills,
                        "matched": matched,
                        "missing": missing,
                    }
            except Exception:
                error = "The PDF could not be read. Please check that it is a valid, non-password-protected PDF."

    return render_template("index.html", result=result, error=error)

@app.errorhandler(413)
def too_large(_error):
    return render_template("index.html", result=None, error="File is too large. Maximum upload size is 5 MB."), 413

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2

app = Flask(__name__)
CORS(app)  # Allow CORS for all domains. Adjust as needed.

def extract_text_from_pdf(file_storage) -> str:
    """Extract text from a PDF file using PyPDF2."""
    # file_storage is an instance of Werkzeug's FileStorage
    pdf_reader = PyPDF2.PdfReader(file_storage)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    # Reset file pointer if needed later
    file_storage.seek(0)
    return text

def score_candidate(resume_text: str, skills: list) -> int:
    """Simple scoring: count occurrences of each required skill (case insensitive)."""
    score = 0
    for skill in skills:
        if skill.lower() in resume_text.lower():
            score += 1
    return score

@app.route("/parse-resumes", methods=["POST"])
def parse_resumes():
    # Get list of uploaded files and required_skills from the form data
    files = request.files.getlist("files")
    required_skills = request.form.get("required_skills", "")
    # Parse skills from a comma-separated string
    skills = [s.strip() for s in required_skills.split(",") if s.strip()]

    candidates = []
    for file_storage in files:
        text = extract_text_from_pdf(file_storage)
        candidate_score = score_candidate(text, skills)
        candidates.append({
            "filename": file_storage.filename,
            "score": candidate_score,
            # Optionally, you can add more details if needed
        })

    # Sort candidates by score (highest first)
    sorted_candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
    return jsonify({"candidates": sorted_candidates})

if __name__ == "__main__":
    app.run(debug=True)

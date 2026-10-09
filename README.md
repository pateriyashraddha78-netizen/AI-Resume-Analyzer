# ResumeIQ — AI-Assisted Resume Analyzer

A beginner-friendly Flask web app that extracts text from a PDF resume and compares detected skills against a pasted job description.

> **Important:** This starter project uses keyword matching, not a trained AI model or an external LLM. The percentage is a simple keyword-overlap estimate and must not be treated as a hiring prediction.

## Features
- Upload a text-based PDF resume (up to 5 MB).
- Paste a job description.
- Extract text from the PDF with `pypdf`.
- Detect skills from a built-in keyword list.
- Display matching skills, potentially missing skills, and an estimated overlap score.
- Responsive interface built with HTML and CSS.
- Uploaded files are processed in memory and are not saved to a database.

## Tech stack
- Python 3.10+
- Flask
- pypdf
- HTML5 and CSS3

## Run locally
1. Install Python 3.10 or newer.
2. Create and activate a virtual environment.

**Windows**
```bash
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies: `pip install -r requirements.txt`
4. Start the application: `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

## How the score works
The app identifies skills from a small built-in list in the resume and job description. It calculates matched required skills divided by detected required skills, multiplied by 100. This is only a keyword overlap metric. It does not evaluate experience, context, proficiency, or candidate suitability.

## Limitations
- Scanned/image-only PDFs may not contain extractable text; OCR is not included.
- The skill list is intentionally small and can be extended in `app.py`.
- This is a portfolio/learning demo, not a production hiring system.
- Do not upload sensitive personal information to public or untrusted deployments.

## Project structure
```text
AI-Resume-Analyzer/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/index.html
└── static/style.css
```

## License
Choose a license before distributing this project publicly.

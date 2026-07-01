# AI Resume Screening System

A simple Flask-based web application that matches a candidate's resume against a job description and returns a similarity score, helping recruiters quickly shortlist relevant resumes.

## Features

- Upload a resume in PDF format
- Paste a job description as text
- Extracts and cleans text from the resume
- Calculates a match score (0–100%) using TF-IDF and Cosine Similarity
- Simple, clean web interface

## Demo

Upload your resume PDF, enter a job description, and click **Check Match** to instantly see how well your resume matches the job.

## Tech Stack

- **Backend:** Python, Flask
- **PDF Parsing:** pdfplumber
- **Text Preprocessing:** Python `re` (Regex)
- **Matching Algorithm:** scikit-learn (TF-IDF Vectorizer + Cosine Similarity)
- **Frontend:** HTML, CSS, JavaScript, Jinja2 templating

## Project Structure

```
AI-Resume-Screening-System/
│
├── app.py                # Main Flask application (routes & orchestration)
├── parser.py              # Extracts text from PDF resumes
├── preprocess.py           # Cleans and normalizes text
├── matcher.py              # Calculates similarity score using TF-IDF + Cosine Similarity
│
├── resumes/                # Folder where uploaded resumes are stored
│
├── static/
│   ├── style.css            # Styling for the web app
│   ├── script.js             # Frontend JavaScript
│   └── p.png                  # Background image
│
└── templates/
    └── index.html             # Main HTML page (upload form + result)
```

## How It Works

1. User uploads a resume (PDF) and enters a job description on the homepage.
2. The resume file is saved to the `resumes/` folder.
3. `parser.py` extracts raw text from the PDF using **pdfplumber**.
4. `preprocess.py` cleans the text (lowercase, removes special characters and extra spaces).
5. `matcher.py` converts both the resume text and job description into TF-IDF vectors and calculates the **cosine similarity** between them.
6. The similarity score is converted into a percentage and displayed on the page.

## Installation & Setup

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/AI-Resume-Screening-System.git
   cd AI-Resume-Screening-System
   ```

2. Create a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install flask pdfplumber scikit-learn
   ```

4. Run the application
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Requirements

```
flask
pdfplumber
scikit-learn
```

(You can save this as `requirements.txt` in the project root.)

##
Made with Flask, Python, and a passion for solving real-world hiring problems.

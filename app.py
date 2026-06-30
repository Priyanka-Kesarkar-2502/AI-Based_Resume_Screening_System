from flask import Flask, render_template, request
import os
from parser import extract_text
from preprocess import preprocess_text
from matcher import calculate_similarity
app = Flask(__name__)
UPLOAD_FOLDER = "resumes"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/match", methods=["POST"])
def match():

    resume = request.files["resume"]

    jd = request.form["job_description"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(filepath)

    resume_text = extract_text(filepath)

    resume_text = preprocess_text(resume_text)

    jd = preprocess_text(jd)

    score = calculate_similarity(
        resume_text,
        jd
    )

    return render_template(
        "index.html",
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)
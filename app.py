from flask import Flask, render_template, request, send_file

from utils.analyzer import analyze_resume, recommend_career
from utils.resume_parser import extract_text_from_pdf
from utils.report_generator import generate_report


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/analyzer")
def analyzer():

    return render_template("analyzer.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    job_role = request.form.get("job_role")

    resume_text = request.form.get("resume_text", "")

    resume_file = request.files.get("resume_file")


    # Check if a PDF was uploaded
    if resume_file and resume_file.filename:

        if resume_file.filename.lower().endswith(".pdf"):

            resume_text = extract_text_from_pdf(resume_file)

        else:

            return "Please upload a PDF file only."


    # Make sure job role is selected
    if not job_role:

        return "Please select a target job role."


    # Make sure resume content exists
    if not resume_text.strip():

        return "Please upload a PDF resume or paste your resume text."


    # Analyze resume
    result = analyze_resume(
    resume_text,
    job_role
)

    career_recommendation = recommend_career(
    resume_text
)
    result["career_recommendation"] = career_recommendation

    return render_template(
        "result.html",
        result=result,
        job_role=job_role,
        career_recommendation=career_recommendation
)


@app.route("/download-report", methods=["POST"])
def download_report():

    job_role = request.form.get("job_role")

    resume_text = request.form.get("resume_text", "")


    # Make sure resume content exists
    if not resume_text.strip():

        return "Resume content is missing."


    # Analyze resume
    result = analyze_resume(
        resume_text,
        job_role
    )


    filename = "resume_analysis_report.pdf"


    # Generate PDF report
    generate_report(
        result,
        job_role,
        filename
    )


    # Download PDF
    return send_file(
        filename,
        as_attachment=True,
        download_name="SmartCareer_AI_Resume_Report.pdf"
    )


if __name__ == "__main__":

    app.run(debug=True)
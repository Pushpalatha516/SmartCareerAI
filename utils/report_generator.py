from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


def generate_report(result, job_role, filename):

    document = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    content = []

    # Title
    content.append(
        Paragraph(
            "SmartCareer AI - Resume Analysis Report",
            title_style
        )
    )

    content.append(Spacer(1, 20))

    # Job Role
    content.append(
        Paragraph(
            f"<b>Target Job Role:</b> {job_role.replace('_', ' ').title()}",
            normal_style
        )
    )

    content.append(Spacer(1, 15))

    # Score
    content.append(
        Paragraph(
            f"<b>Job Readiness Score:</b> {result['score']}%",
            heading_style
        )
    )
        # Career Recommendation

    if "career_recommendation" in result:

        content.append(
            Paragraph(
                "Career Recommendation",
                heading_style
            )
        )

        recommended_role = (
            result["career_recommendation"]
            .get("recommended_role", "")
            .replace("_", " ")
            .title()
        )

        content.append(
            Paragraph(
                f"<b>Recommended Career:</b> {recommended_role}",
                normal_style
            )
        )

        content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            f"<b>Readiness:</b> {result['readiness']}",
            normal_style
        )
    )

    content.append(Spacer(1, 10))

    # Summary
    content.append(
        Paragraph(
            f"<b>Summary:</b> {result['summary']}",
            normal_style
        )
    )

    content.append(Spacer(1, 20))

    # Career Recommendation

    if "career_recommendation" in result:

        content.append(
            Paragraph(
                "Career Recommendation",
                heading_style
            )
        )

        recommended_role = (
            result["career_recommendation"]
            .get("recommended_role", "")
            .replace("_", " ")
            .title()
        )

        content.append(
            Paragraph(
                f"<b>Recommended Career:</b> {recommended_role}",
                normal_style
            )
        )

        content.append(Spacer(1, 15))

    # Career Recommendation

    if "career_recommendation" in result:

        content.append(
            Paragraph(
                "Career Recommendation",
                heading_style
            )
        )

        recommended_role = (
            result["career_recommendation"]
            .get("recommended_role", "")
            .replace("_", " ")
            .title()
        )

        content.append(
            Paragraph(
                f"<b>Recommended Career:</b> {recommended_role}",
                normal_style
            )
        )

        content.append(Spacer(1, 15))
    # Matched Skills
    content.append(
        Paragraph(
            "Matched Skills",
            heading_style
        )
    )

    if result["matched_skills"]:

        for skill in result["matched_skills"]:

            content.append(
                Paragraph(
                    f"• {skill}",
                    normal_style
                )
            )

    else:

        content.append(
            Paragraph(
                "No matching skills detected.",
                normal_style
            )
        )

    content.append(Spacer(1, 20))

    # Missing Skills
    content.append(
        Paragraph(
            "Skills to Improve",
            heading_style
        )
    )

    if result["missing_skills"]:

        for skill in result["missing_skills"]:

            content.append(
                Paragraph(
                    f"• {skill}",
                    normal_style
                )
            )

    else:

        content.append(
            Paragraph(
                "No missing skills detected.",
                normal_style
            )
        )

    content.append(Spacer(1, 20))

    # Recommendations
    content.append(
        Paragraph(
            "Recommended Next Steps",
            heading_style
        )
    )

    for item in result["recommendations"]:

        content.append(
            Paragraph(
                f"<b>{item['skill']}</b>: "
                f"{item['recommendation']}",
                normal_style
            )
        )

        content.append(Spacer(1, 8))

    # Interview Questions
    content.append(
        Paragraph(
            "Interview Preparation",
            heading_style
        )
    )

    for item in result["interview_questions"]:

        content.append(
            Paragraph(
                f"<b>{item['skill']}</b>",
                normal_style
            )
        )

        for question in item["questions"]:

            content.append(
                Paragraph(
                    f"• {question}",
                    normal_style
                )
            )

        content.append(Spacer(1, 8))

    # Learning Roadmap
    content.append(
        Paragraph(
            "Learning Roadmap",
            heading_style
        )
    )

    for item in result["learning_roadmaps"]:

        content.append(
            Paragraph(
                f"<b>{item['skill']}</b>",
                normal_style
            )
        )

        for step in item["steps"]:

            content.append(
                Paragraph(
                    f"• {step}",
                    normal_style
                )
            )

        content.append(Spacer(1, 8))

    document.build(content)
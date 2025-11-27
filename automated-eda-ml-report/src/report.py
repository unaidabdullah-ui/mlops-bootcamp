from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(summary, model_results, output_path="reports/final_report.pdf"):
    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Automated EDA & ML Report</b>", styles['Title']))
    story.append(Paragraph("<br/>", styles['Normal']))
    story.append(Paragraph("<b>Dataset Summary:</b><br/>" + summary, styles['Normal']))

    story.append(Paragraph("<br/><b>Model Performance:</b>", styles['Heading2']))

    for model, score in model_results.items():
        story.append(Paragraph(f"{model}: {score}", styles['Normal']))

    doc.build(story)

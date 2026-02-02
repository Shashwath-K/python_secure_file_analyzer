import os
import shutil
import gradio as gr

from app.services.file_analyzer import FileAnalyzer
from app.services.report_generator import ReportGenerator
from app.utils.validators import FileValidator, FileValidationError


UPLOAD_DIR = "uploads"


def process_file(uploaded_file):
    """
    Orchestrates file validation, analysis, and report generation.
    """

    if uploaded_file is None:
        return "No file uploaded.", None

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    saved_file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    shutil.copy(uploaded_file, saved_file_path)

    validator = FileValidator()
    analyzer = FileAnalyzer()
    reporter = ReportGenerator()

    try:
        validator.validate(saved_file_path)
        analysis_result = analyzer.analyze(saved_file_path)
        report_path = reporter.generate(
            analysis_data=analysis_result,
            source_filename=uploaded_file.name,
        )

        summary = (
            "File analysis completed successfully.\n\n"
            f"Lines: {analysis_result['lines']}\n"
            f"Words: {analysis_result['words']}\n"
            f"Characters: {analysis_result['characters']}\n"
            f"Uppercase Characters: {analysis_result['uppercase_characters']}"
        )

        return summary, report_path

    except FileValidationError as ve:
        return f"Validation Error: {str(ve)}", None

    except Exception as e:
        return f"Processing Error: {str(e)}", None


def create_interface():
    """
    Builds and returns the Gradio interface.
    """

    with gr.Blocks(title="Secure File Analyzer & Report Generator") as interface:
        gr.Markdown("## Secure File Analyzer & Report Generator")

        file_input = gr.File(
            label="Upload a text file",
            file_types=[".txt"]
        )

        analyze_button = gr.Button("Analyze File")

        output_text = gr.Textbox(
            label="Analysis Summary",
            lines=10,
            interactive=False
        )

        output_file = gr.File(
            label="Download Analysis Report"
        )

        analyze_button.click(
            fn=process_file,
            inputs=file_input,
            outputs=[output_text, output_file]
        )

    return interface

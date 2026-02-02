import os
import shutil
import gradio as gr

from app.services.file_analyzer import FileAnalyzer
from app.services.report_generator import ReportGenerator
from app.utils.validators import FileValidator, FileValidationError
from app.config import UPLOAD_DIR


def process_file(uploaded_file):
    """
    Orchestrates file validation, analysis, and report generation.
    """

    if uploaded_file is None:
        return "No file uploaded.", None

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Gradio already stores the file on disk
    source_path = uploaded_file.name

    # Extract only the filename (not full temp path)
    filename = os.path.basename(source_path)
    destination_path = os.path.join(UPLOAD_DIR, filename)

    # Copy only if source and destination differ
    if os.path.abspath(source_path) != os.path.abspath(destination_path):
        shutil.copy(source_path, destination_path)
    else:
        destination_path = source_path

    validator = FileValidator()
    analyzer = FileAnalyzer()
    reporter = ReportGenerator()

    try:
        validator.validate(destination_path)
        analysis_result = analyzer.analyze(destination_path)

        report_path = reporter.generate(
            analysis_data=analysis_result,
            source_filename=filename,
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

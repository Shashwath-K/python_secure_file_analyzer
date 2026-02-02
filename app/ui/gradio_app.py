import os
import shutil
import gradio as gr

from app.services.file_analyzer import FileAnalyzer
from app.services.report_generator import ReportGenerator
from app.utils.validators import FileValidator, FileValidationError
from app.config import UPLOAD_DIR


def process_file(uploaded_file):
    if uploaded_file is None:
        return "No file uploaded.", None

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    source_path = uploaded_file.name
    filename = os.path.basename(source_path)
    destination_path = os.path.join(UPLOAD_DIR, filename)

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
    with gr.Blocks(
        title="Secure File Analyzer & Report Generator",
        css="""
        body {
            font-family: Inter, system-ui, sans-serif;
        }
        .container {
            max-width: 900px;
            margin: auto;
        }
        .section {
            padding: 20px;
            border-radius: 10px;
            background-color: #ffffff;
        }
        """
    ) as interface:

        with gr.Column(elem_classes="container"):
            gr.Markdown(
                """
                # Secure File Analyzer & Report Generator
                Analyze text files securely and generate structured reports.
                """
            )

            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("### File Upload")
                    file_input = gr.File(
                        label="Select a text file",
                        file_types=[".txt"]
                    )

                with gr.Column(scale=1):
                    gr.Markdown("### Action")
                    analyze_button = gr.Button(
                        "Analyze File",
                        variant="primary"
                    )

            gr.Markdown("### Analysis Output")

            output_text = gr.Textbox(
                label="Analysis Summary",
                lines=8,
                interactive=False,
                placeholder="Analysis results will appear here"
            )

            output_file = gr.File(
                label="Generated Report"
            )

            analyze_button.click(
                fn=process_file,
                inputs=file_input,
                outputs=[output_text, output_file]
            )

    return interface

import os
from datetime import datetime
from typing import Dict


class ReportGenerator:
    """
    Generates a structured text report based on file analysis results.
    """

    def generate(
        self,
        analysis_data: Dict[str, int],
        source_filename: str,
        output_dir: str = "reports",
    ) -> str:
        """
        Generate and save a text-based analysis report.

        Args:
            analysis_data (Dict[str, int]): Analysis metrics.
            source_filename (str): Original uploaded file name.
            output_dir (str): Directory to store generated reports.

        Returns:
            str: Path to the generated report file.
        """

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_filename = f"analysis_report_{timestamp}.txt"
        report_path = os.path.join(output_dir, report_filename)

        with open(report_path, "w", encoding="utf-8") as report:
            report.write("Secure File Analysis Report\n")
            report.write("=" * 30 + "\n\n")

            report.write(f"Source File      : {source_filename}\n")
            report.write(f"Generated On     : {timestamp}\n\n")

            report.write("Analysis Summary\n")
            report.write("-" * 20 + "\n")
            report.write(f"Total Lines              : {analysis_data['lines']}\n")
            report.write(f"Total Words              : {analysis_data['words']}\n")
            report.write(f"Total Characters         : {analysis_data['characters']}\n")
            report.write(
                f"Uppercase Characters     : {analysis_data['uppercase_characters']}\n"
            )

        return report_path

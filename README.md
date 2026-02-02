# Secure File Analyzer & Report Generator

## Project Overview

Secure File Analyzer & Report Generator is a Python-based utility designed to perform structured analysis of text files and produce a downloadable summary report. The application provides a graphical interface using the Gradio framework and focuses on correctness, robustness, and maintainability.

The system is intended for environments where file content inspection, validation, and reporting are required, such as academic analysis, preprocessing pipelines, internal utilities, or secure document assessment tools.

---

## Objectives

The primary objectives of this project are:

* To analyze uploaded text files using reliable file-handling techniques
* To extract meaningful statistical metrics from file content
* To detect and handle invalid or empty files safely
* To generate a structured analysis report for download
* To demonstrate clean software architecture aligned with industry standards

---

## Key Features

* Secure upload and handling of text files
* Line count computation
* Word count computation
* Character count computation
* Uppercase letter detection and counting
* Validation for empty, corrupted, or unsupported files
* Automatic generation of a human-readable analysis report
* Downloadable report output
* Modular and testable codebase

---

## Technology Stack

* Programming Language: Python 3.x
* User Interface Framework: Gradio
* Runtime Environment: Local execution (cross-platform)
* File Handling: Native Python file I/O

---

## Architectural Design

The project follows a layered architecture that separates responsibilities across distinct modules:

* Presentation Layer: Handles user interaction through Gradio UI
* Service Layer: Implements core business logic for analysis and reporting
* Utility Layer: Provides validation and helper functions
* Configuration Layer: Centralizes application settings

This structure promotes scalability, maintainability, and ease of testing.

---

## Project Structure

```
secure-file-analyzer/
│
├── app/
│   ├── ui/
│   │   └── gradio_app.py
│   │
│   ├── services/
│   │   ├── file_analyzer.py
│   │   └── report_generator.py
│   │
│   ├── utils/
│   │   └── validators.py
│   │
│   └── config.py
│
├── uploads/
├── reports/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Functional Workflow

1. The user uploads a text file through the Gradio interface.
2. The file undergoes validation checks:

   * File existence
   * File size
   * Content integrity
3. The validated file is processed line-by-line to compute:

   * Total number of lines
   * Total number of words
   * Total number of characters
   * Total number of uppercase characters
4. The computed metrics are passed to the report generation service.
5. A structured report is generated and stored in the reports directory.
6. The user downloads the generated report.

---

## Core Concepts Applied

* File Handling

  * File pointers
  * Safe opening and closing of files
  * Line-based reading for memory efficiency

* Software Engineering Practices

  * Separation of concerns
  * Modular design
  * Readability and maintainability
  * Test-oriented structure

---

## Installation and Setup

### Prerequisites

* Python 3.8 or higher
* pip package manager
* Virtual environment support (recommended)

### Setup Instructions

1. Clone the repository

   ```
   git clone "https://github.com/Shashwath-K/python_secure_file_analyzer.git"
   cd secure-file-analyzer
   ```

2. Create and activate a virtual environment

   Windows:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   Linux or macOS:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies

   ```
   pip install -r requirements.txt
   ```

---

## Running the Application

To start the application, execute:

```
python main.py
```

Once started, Gradio will provide a local URL that can be accessed via a web browser.

---

## Output Report Format

The generated report contains:

* File name
* File size
* Total number of lines
* Total number of words
* Total number of characters
* Total number of uppercase characters
* Processing timestamp
* Validation status

The report is stored locally and made available for download.

---

## Error Handling and Validation

The application explicitly handles:

* Empty files
* Unsupported file formats
* Read permission errors
* Invalid or corrupted content
* Runtime I/O exceptions

Clear and deterministic feedback is provided to the user.

---

## Testing Strategy

* Unit tests are located in the tests directory
* Tests cover:

  * File validation logic
  * Content analysis accuracy
* The architecture allows straightforward extension to integration testing

---

## Security Considerations

* Uploaded files are processed locally
* No external transmission of file contents
* Controlled upload and storage directories
* Minimal file permissions required

---

## Extensibility

The project is designed to support future enhancements, including:

* PDF or JSON report formats
* Encrypted file handling
* Logging and audit trails
* Multi-file batch processing
* Role-based access control

---

## Intended Use Cases

* Academic projects and coursework
* Internal tooling and automation
* Preprocessing utilities for NLP pipelines
* Demonstration of file-handling concepts
* Secure offline text analysis

---

## License

This project is provided for educational and internal use. Licensing terms may be defined as required.

---

## Author and Maintenance

Maintained as a structured, professional-grade Python utility with emphasis on clarity, correctness, and scalability.

---

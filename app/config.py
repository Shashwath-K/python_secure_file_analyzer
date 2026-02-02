import os


# Base directory of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# Directory paths
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
REPORT_DIR = os.path.join(BASE_DIR, "reports")


# File handling configuration
ALLOWED_EXTENSIONS = {".txt"}
MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB limit


# Application metadata
APP_NAME = "Secure File Analyzer & Report Generator"
APP_VERSION = "1.0.0"


def ensure_directories() -> None:
    """
    Ensure that required application directories exist.
    """

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)

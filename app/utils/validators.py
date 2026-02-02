import os


class FileValidationError(Exception):
    """
    Custom exception for file validation failures.
    """
    pass


class FileValidator:
    """
    Provides validation utilities for uploaded files.
    """

    ALLOWED_EXTENSIONS = {".txt"}

    def validate(self, file_path: str) -> None:
        """
        Validate the given file before analysis.

        Args:
            file_path (str): Path to the file.

        Raises:
            FileValidationError: If validation fails.
        """

        if not file_path:
            raise FileValidationError("No file path provided.")

        if not os.path.exists(file_path):
            raise FileValidationError("File does not exist.")

        if not os.path.isfile(file_path):
            raise FileValidationError("Invalid file type.")

        _, ext = os.path.splitext(file_path)
        if ext.lower() not in self.ALLOWED_EXTENSIONS:
            raise FileValidationError("Unsupported file format. Only .txt files are allowed.")

        if os.path.getsize(file_path) == 0:
            raise FileValidationError("Uploaded file is empty.")

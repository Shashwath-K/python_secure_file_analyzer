import os
import tempfile
import pytest

from app.utils.validators import FileValidator, FileValidationError


def test_valid_file_passes_validation():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as tmp:
        tmp.write("Valid content")
        tmp_path = tmp.name

    validator = FileValidator()
    validator.validate(tmp_path)

    os.remove(tmp_path)


def test_empty_file_fails_validation():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as tmp:
        tmp_path = tmp.name

    validator = FileValidator()

    with pytest.raises(FileValidationError):
        validator.validate(tmp_path)

    os.remove(tmp_path)


def test_invalid_extension_fails_validation():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".pdf") as tmp:
        tmp.write("Invalid format")
        tmp_path = tmp.name

    validator = FileValidator()

    with pytest.raises(FileValidationError):
        validator.validate(tmp_path)

    os.remove(tmp_path)


def test_missing_file_fails_validation():
    validator = FileValidator()

    with pytest.raises(FileValidationError):
        validator.validate("non_existent_file.txt")

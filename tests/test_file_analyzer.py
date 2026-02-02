import os
import tempfile

from app.services.file_analyzer import FileAnalyzer


def test_file_analysis_basic_metrics():
    content = "Hello World\nTHIS is A Test\n"

    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    analyzer = FileAnalyzer()
    result = analyzer.analyze(tmp_path)

    os.remove(tmp_path)

    assert result["lines"] == 2
    assert result["words"] == 6
    assert result["characters"] == len(content)
    assert result["uppercase_characters"] == sum(1 for c in content if c.isupper())


def test_file_analysis_empty_file():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as tmp:
        tmp_path = tmp.name

    analyzer = FileAnalyzer()
    result = analyzer.analyze(tmp_path)

    os.remove(tmp_path)

    assert result["lines"] == 0
    assert result["words"] == 0
    assert result["characters"] == 0
    assert result["uppercase_characters"] == 0

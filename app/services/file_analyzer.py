from typing import Dict


class FileAnalyzer:
    """
    Performs content analysis on a text file.

    Metrics computed:
    - Total lines
    - Total words
    - Total characters
    - Total uppercase characters
    """

    def analyze(self, file_path: str) -> Dict[str, int]:
        """
        Analyze the contents of a text file.

        Args:
            file_path (str): Path to the text file.

        Returns:
            Dict[str, int]: Dictionary containing analysis metrics.

        Raises:
            IOError: If the file cannot be read.
        """

        line_count = 0
        word_count = 0
        char_count = 0
        uppercase_count = 0

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line_count += 1
                char_count += len(line)

                words = line.split()
                word_count += len(words)

                for char in line:
                    if char.isupper():
                        uppercase_count += 1

        return {
            "lines": line_count,
            "words": word_count,
            "characters": char_count,
            "uppercase_characters": uppercase_count,
        }

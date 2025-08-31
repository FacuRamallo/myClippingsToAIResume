import os
import logging
import re
from src.infrastructure.file_interfaces import FileReader, FileWriter

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class LocalFileReader(FileReader):
    """
    Implementation of FileReader for local file system.
    """

    def read(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

class LocalFileWriter(FileWriter):
    """
    Implementation of FileWriter for local file system.
    """

    def write(self, file_path: str, content: str):
        logger.debug("Writing to file: %s", file_path)
        logger.debug("Content: %s", content[:100])  # Log first 100 characters of content
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

def format_to_markdown_list(input_text: str) -> str:
    """
    Convert a string with bullet points into a Markdown list.

    Args:
        input_text (str): The input string containing bullet points.

    Returns:
        str: The formatted Markdown list.
    """
    # Regular expression to match bullet points starting with "•"
    bullet_pattern = r"•\s*([^•]+)"

    # Replace bullet points with Markdown list items
    formatted_text = re.sub(bullet_pattern, r"- \1", input_text)

    return formatted_text



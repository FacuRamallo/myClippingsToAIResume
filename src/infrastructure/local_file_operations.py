import os
import logging
import re
from src.infrastructure.file_interfaces import FileReader, FileWriter
from src.infrastructure.MarkdownBookFormatter import MarkdownBookFormatter

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

    def write(self, output_dir: str, books):
        formatter = MarkdownBookFormatter()
        for book in books:
            logger.debug("Formatting and writing book: %s by %s", book.title.value, book.author.value)

            # Sanitize the book title for the filename
            safe_title = "".join(c for c in book.title.value if c.isalnum() or c in (" ", "-", "_")).rstrip()
            file_path = os.path.join(output_dir, f"{safe_title}.md")

            # Format the book into Markdown content
            content = formatter.format(book)

            # Write to file
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

            logger.debug("Markdown file written to: %s", file_path)



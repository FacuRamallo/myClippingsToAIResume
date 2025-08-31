import os
from typing import Dict, List
from src.infrastructure.file_interfaces import FileWriter
import logging

# Configure logging
logger = logging.getLogger(__name__)

class MarkdownGenerator:
    """
    A class to generate Markdown files for each book.
    """

    def __init__(self, output_dir: str, file_writer: FileWriter):
        """
        Initialize the MarkdownGenerator.

        Args:
            output_dir (str): The directory where Markdown files will be saved.
            file_writer (FileWriter): The file writer implementation.
        """
        self.output_dir = output_dir
        self.file_writer = file_writer
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_markdown(self, book_title: str, author: str, highlights: List[Dict[str, str]]):
        """
        Generate a Markdown file for a book.

        Args:
            book_title (str): The title of the book.
            author (str): The author of the book.
            highlights (List[Dict[str, str]]): A list of highlights for the book.
        """
        logger.debug("Output directory: %s", self.output_dir)
        logger.debug("Generating Markdown for book: %s by %s", book_title, author)
        logger.debug("Highlights: %s", highlights)

        # Sanitize the book title for the filename
        safe_title = self._sanitize_filename(book_title)
        file_path = os.path.join(self.output_dir, f"{safe_title}.md")
        logger.debug("Full file path: %s", file_path)

        # Create the Markdown content
        content = self._create_markdown_content(book_title, author, highlights)

        # Write to file
        self.file_writer.write(file_path, content)
        logger.debug("Markdown file written to: %s", file_path)

    def _create_markdown_content(self, book_title: str, author: str, highlights: List[Dict[str, str]]) -> str:
        """
        Create the Markdown content for a book.

        Args:
            book_title (str): The title of the book.
            author (str): The author of the book.
            highlights (List[Dict[str, str]]): A list of highlights for the book.

        Returns:
            str: The Markdown content.
        """
        # Metadata header
        header = f"""# {book_title}

**Author:** {author}

---

"""

        # Highlights
        highlights_md = "\n\n".join(
            [f"- **Location {h['location']}**: {h['highlight']}" for h in highlights]
        )

        return header + highlights_md

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize a string to be used as a filename.

        Args:
            name (str): The string to sanitize.

        Returns:
            str: The sanitized string.
        """
        return "".join(c for c in name if c.isalnum() or c in (" ", "-", "_")).rstrip()

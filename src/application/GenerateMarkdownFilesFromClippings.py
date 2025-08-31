import os
from typing import List
from src.infrastructure.file_interfaces import FileReader, FileWriter
from src.domain.clippings_parser import ClippingsParserService
import logging

# Configure logging
logger = logging.getLogger(__name__)

class GenerateMarkdownFilesFromClippings:
    """
    Use case for generating Markdown files from Kindle clippings.
    """

    def __init__(self, output_dir: str, input_file_path: str, file_reader: FileReader, file_writer: FileWriter):
        """
        Initialize the use case.

        Args:
            output_dir (str): The directory where Markdown files will be saved.
            input_file_path (str): The path to the input clippings file.
            file_reader (FileReader): The file reader implementation.
            file_writer (FileWriter): The file writer implementation.
        """
        self.output_dir = output_dir
        self.input_file_path = input_file_path
        self.file_reader = file_reader
        self.file_writer = file_writer
        os.makedirs(self.output_dir, exist_ok=True)

    def execute(self):
        """
        Execute the use case to generate Markdown files from Kindle clippings.
        """
        logger.debug("Reading input file: %s", self.input_file_path)
        file_content = self.file_reader.read(self.input_file_path)

        logger.debug("Parsing clippings content.")
        parser = ClippingsParserService()
        books = parser.parse_to_entities(file_content)

        logger.debug("Generating Markdown files for each book.")
        for book in books:
            self._generate_markdown(book)

    def _generate_markdown(self, book):
        """
        Generate a Markdown file for a book.

        Args:
            book (Book): The book entity containing title, author, and clippings.
        """
        logger.debug("Generating Markdown for book: %s by %s", book.title.value, book.author.value)

        # Sanitize the book title for the filename
        safe_title = self._sanitize_filename(book.title.value)
        file_path = os.path.join(self.output_dir, f"{safe_title}.md")

        # Create the Markdown content
        content = self._create_markdown_content(
            book.title.value,
            book.author.value,
            [
                {
                    "location": clipping.location.value,
                    "highlight": clipping.highlight.value
                }
                for clipping in book.clippings
            ]
        )

        # Write to file
        self.file_writer.write(file_path, content)
        logger.debug("Markdown file written to: %s", file_path)

    def _format_to_markdown_list(self, input_text: str) -> str:
        """
        Convert a string with bullet points into a properly indented Markdown list.

        Args:
            input_text (str): The input string containing bullet points.

        Returns:
            str: The formatted Markdown list.
        """
        import re
        # Regular expression to match bullet points starting with "•"
        bullet_pattern = r"•\s*([^•]+)"

        # Replace bullet points with Markdown list items, ensuring proper indentation
        formatted_text = re.sub(bullet_pattern, r"\n  - \1", input_text)

        return formatted_text

    def _create_markdown_content(self, book_title: str, author: str, highlights: List[dict]) -> str:
        """
        Create the Markdown content for a book.

        Args:
            book_title (str): The title of the book.
            author (str): The author of the book.
            highlights (List[dict]): A list of highlights for the book.

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
            [
                f"- **Location {h['location']}**:\n{self._format_to_markdown_list(h['highlight'])}"
                for h in highlights
            ]
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

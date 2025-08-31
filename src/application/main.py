import os
from typing import List
from dotenv import load_dotenv
import logging

from src.domain.clippings_parser import ClippingsParserService
from src.domain.entities import Book, Clipping
from src.domain.value_objects import Title, Author, Location, CreatedAt, Highlight
from src.application.markdown_generator import MarkdownGenerator
from src.infrastructure.local_file_operations import LocalFileWriter

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ClippingsUseCase:
    """
    Use case for processing Kindle clippings and generating output files.
    """

    def __init__(self, parser: ClippingsParserService, generator: MarkdownGenerator):
        """
        Initialize the use case with dependencies.

        Args:
            parser (ClippingsParserService): The service for parsing clippings.
            generator (MarkdownGenerator): The service for generating Markdown files.
        """
        self.parser = parser
        self.generator = generator

    def process_clippings(self, clippings_file: str, output_dir: str):
        """
        Process the clippings file and generate output files.

        Args:
            clippings_file (str): Path to the "My Clippings.txt" file.
            output_dir (str): Directory to save the output files.
        """
        # Parse raw DTOs
        raw_clippings = self.parser.parse_to_dto(clippings_file)

        # Transform DTOs into domain entities
        books = self._map_to_books(raw_clippings)

        # Generate Markdown files for each book
        for book in books:
            self.generator.generate_markdown(
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

    def _map_to_books(self, raw_clippings: List[dict]) -> List[Book]:
        """
        Map raw clippings data to domain entities.

        Args:
            raw_clippings (List[dict]): Raw clippings data.

        Returns:
            List[Book]: A list of Book entities.
        """
        books_dict = {}
        for raw in raw_clippings:
            title = Title(raw["title"])
            author = Author(raw["author"])
            clipping = Clipping(
                title=title,
                author=author,
                location=Location(raw["location"]),
                created_at=CreatedAt("Unknown"),  # Placeholder for CreatedAt
                highlight=Highlight(raw["highlight"])
            )

            book_key = (title.value, author.value)
            if book_key not in books_dict:
                books_dict[book_key] = Book(title=title, author=author, clippings=[])

            books_dict[book_key].clippings.append(clipping)

        return list(books_dict.values())

def generate_markdown_files(clippings_file: str, output_dir: str):
    """
    Parse clippings and generate Markdown files for each book.

    Args:
        clippings_file (str): Path to the "My Clippings.txt" file.
        output_dir (str): Directory to save the Markdown files.
    """
    logger.debug("Starting to process clippings file: %s", clippings_file)

    # Parse raw DTOs
    parser = ClippingsParserService()
    raw_clippings = parser.parse_to_dto(clippings_file)
    logger.debug("Parsed raw clippings: %s", raw_clippings)

    # Map raw DTOs to domain entities
    books_dict = {}
    for raw in raw_clippings:
        title = Title(raw["title"])
        author = Author(raw["author"])
        clipping = Clipping(
            title=title,
            author=author,
            location=Location(raw["location"]),
            created_at=CreatedAt("Unknown"),  # Placeholder for CreatedAt
            highlight=Highlight(raw["highlight"])
        )

        book_key = (title.value, author.value)
        if book_key not in books_dict:
            books_dict[book_key] = Book(title=title, author=author, clippings=[])

        books_dict[book_key].clippings.append(clipping)

    books = list(books_dict.values())
    logger.debug("Mapped books: %s", books)

    # Initialize Markdown generator with a file writer
    file_writer = LocalFileWriter()
    generator = MarkdownGenerator(output_dir, file_writer)

    # Generate Markdown files for each book
    for book in books:
        logger.debug("Generating Markdown for book: %s", book.title.value)
        generator.generate_markdown(
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
    logger.debug("Markdown generation completed.")

def get_env_variable(var_name: str, default: str) -> str:
    """
    Get the value of an environment variable or return a default value.

    Args:
        var_name (str): The name of the environment variable.
        default (str): The default value to return if the variable is not set.

    Returns:
        str: The value of the environment variable or the default value.
    """
    return os.getenv(var_name, default)

if __name__ == "__main__":
    # Configure paths using environment variables
    clippings_file = get_env_variable("CLIPPINGS_FILE", "input_files/My Clippings.txt")
    output_dir = get_env_variable("OUTPUT_DIR", "processed_files_output")

    # Ensure the input and output directories exist
    input_dir = os.path.dirname(clippings_file)
    output_dir_path = os.path.abspath(output_dir)

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir_path, exist_ok=True)

    if not os.path.exists(clippings_file):
        print(f"Clippings file not found: {clippings_file}")
    else:
        generate_markdown_files(clippings_file, output_dir)
        print(f"Markdown files generated in: {output_dir}")

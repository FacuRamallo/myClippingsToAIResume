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
        books = parser.parse_to_books(file_content)

        logger.debug("Generating Markdown files for each book.")
        self.file_writer.write(self.output_dir, books)

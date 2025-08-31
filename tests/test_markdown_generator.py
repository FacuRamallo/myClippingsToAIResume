import pytest
import os
from src.application.main import generate_markdown_files
from src.infrastructure.local_file_operations import LocalFileWriter
from src.application.markdown_generator import MarkdownGenerator

@pytest.fixture
def sample_clippings_file(tmp_path):
    content = """Book Title (Author Name)
- Your Highlight on Location 123-124 | Added on Thursday, January 1, 1970 12:00:00 AM

This is a sample highlight.
==========
Book Title (Author Name)
- Your Highlight on Location 125-126 | Added on Thursday, January 1, 1970 12:00:00 AM

This is another highlight for the same book.
==========
Another Book (Another Author)
- Your Highlight on Location 456 | Added on Thursday, January 1, 1970 12:00:00 AM

Another highlight text.
=========="""
    file_path = tmp_path / "My Clippings.txt"
    file_path.write_text(content, encoding="utf-8")
    return file_path

@pytest.fixture
def output_dir(tmp_path):
    return tmp_path / "output"

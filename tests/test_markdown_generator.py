import pytest
import os
from src.application.main import generate_markdown_files

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

def test_generate_markdown_files(sample_clippings_file, output_dir):
    # Run the Markdown generation
    generate_markdown_files(str(sample_clippings_file), str(output_dir))

    # Check if files are created
    book1_file = output_dir / "Book Title.md"
    book2_file = output_dir / "Another Book.md"

    assert book1_file.exists()
    assert book2_file.exists()

    # Validate content of Book Title.md
    book1_content = book1_file.read_text(encoding="utf-8")
    assert "# Book Title" in book1_content
    assert "**Author:** Author Name" in book1_content
    assert "**Location 123-124**: This is a sample highlight." in book1_content
    assert "**Location 125-126**: This is another highlight for the same book." in book1_content

    # Validate content of Another Book.md
    book2_content = book2_file.read_text(encoding="utf-8")
    assert "# Another Book" in book2_content
    assert "**Author:** Another Author" in book2_content
    assert "**Location 456**: Another highlight text." in book2_content

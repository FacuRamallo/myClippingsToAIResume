import os
import pytest
from datetime import datetime
from src.infrastructure.local_file_operations import LocalFileReader, LocalFileWriter
from src.domain.entities import Book, Title, Author, Clipping, Location, Highlight

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Sample content")
    return file_path

@pytest.fixture
def sample_books():
    return [
        Book(
            title=Title("Sample Book"),
            author=Author("Sample Author"),
            clippings=[
                Clipping(
                    title=Title("Sample Book"),
                    author=Author("Sample Author"),
                    location=Location("123-124"),
                    highlight=Highlight("This is a sample highlight."),
                    created_at=datetime(2025, 8, 31, 12, 0, 0)
                )
            ]
        )
    ]

def test_local_file_reader(sample_file):
    reader = LocalFileReader()
    content = reader.read(str(sample_file))
    assert content == "Sample content"

def test_local_file_writer(tmp_path, sample_books):
    writer = LocalFileWriter()
    output_dir = tmp_path / "output"
    writer.write(str(output_dir), sample_books)

    # Verify the file was created
    file_path = output_dir / "Sample Book.md"
    assert file_path.exists()

    # Verify the content
    content = file_path.read_text()
    assert "# Sample Book" in content
    assert "**Author:** Sample Author" in content
    assert "- **Location 123-124**:" in content
    assert "This is a sample highlight." in content

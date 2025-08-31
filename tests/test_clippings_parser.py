import pytest
from src.domain.clippings_parser import ClippingsParserService
from datetime import datetime

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

def test_parse_clippings(sample_clippings_file):
    parser = ClippingsParserService()

    # Read the file content to pass as a string
    file_content = sample_clippings_file.read_text(encoding="utf-8")

    books = parser.parse_to_entities(file_content)

    assert len(books) == 2

    # Validate the first book
    book1 = books[0]
    assert book1.title.value == "Book Title"
    assert book1.author.value == "Author Name"
    assert len(book1.clippings) == 2

    clipping1 = book1.clippings[0]
    assert clipping1.location.value == "123-124"
    assert clipping1.highlight.value == "This is a sample highlight."
    assert clipping1.created_at.value == datetime(1970, 1, 1, 0, 0, 0)

    clipping2 = book1.clippings[1]
    assert clipping2.location.value == "125-126"
    assert clipping2.highlight.value == "This is another highlight for the same book."
    assert clipping2.created_at.value == datetime(1970, 1, 1, 0, 0, 0)

    # Validate the second book
    book2 = books[1]
    assert book2.title.value == "Another Book"
    assert book2.author.value == "Another Author"
    assert len(book2.clippings) == 1

    clipping3 = book2.clippings[0]
    assert clipping3.location.value == "456"
    assert clipping3.highlight.value == "Another highlight text."
    assert clipping3.created_at.value == datetime(1970, 1, 1, 0, 0, 0)

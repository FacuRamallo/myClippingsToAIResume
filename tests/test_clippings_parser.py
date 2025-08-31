import pytest
from src.domain.clippings_parser import ClippingsParserService

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
    raw_clippings = parser.parse_to_dto(sample_clippings_file)

    assert len(raw_clippings) == 3

    # Validate the first raw clipping
    clipping1 = raw_clippings[0]
    assert clipping1["title"] == "Book Title"
    assert clipping1["author"] == "Author Name"
    assert clipping1["location"] == "123-124"
    assert clipping1["highlight"] == "This is a sample highlight."

    # Validate the second raw clipping
    clipping2 = raw_clippings[1]
    assert clipping2["location"] == "125-126"
    assert clipping2["highlight"] == "This is another highlight for the same book."

    # Validate the third raw clipping
    clipping3 = raw_clippings[2]
    assert clipping3["title"] == "Another Book"
    assert clipping3["author"] == "Another Author"
    assert clipping3["location"] == "456"
    assert clipping3["highlight"] == "Another highlight text."

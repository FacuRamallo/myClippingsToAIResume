import pytest
from src.domain.clippings_parser import ClippingsParser

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
    parser = ClippingsParser()
    clippings = parser.parse(sample_clippings_file)

    assert len(clippings) == 3

    assert clippings[0]["title"] == "Book Title"
    assert clippings[0]["author"] == "Author Name"
    assert clippings[0]["location"] == "123-124"
    assert clippings[0]["highlight"] == "This is a sample highlight."

    assert clippings[1]["title"] == "Book Title"
    assert clippings[1]["author"] == "Author Name"
    assert clippings[1]["location"] == "125-126"
    assert clippings[1]["highlight"] == "This is another highlight for the same book."

    assert clippings[2]["title"] == "Another Book"
    assert clippings[2]["author"] == "Another Author"
    assert clippings[2]["location"] == "456"
    assert clippings[2]["highlight"] == "Another highlight text."

def test_group_by_book(sample_clippings_file):
    parser = ClippingsParser()
    clippings = parser.parse(sample_clippings_file)
    grouped = parser.group_by_book(clippings)

    assert len(grouped) == 2
    assert "Book Title" in grouped
    assert "Another Book" in grouped
    assert len(grouped["Book Title"]) == 2
    assert len(grouped["Another Book"]) == 1

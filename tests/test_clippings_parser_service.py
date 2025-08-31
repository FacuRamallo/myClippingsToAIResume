import pytest
from datetime import datetime
from src.domain.clippings_parser import ClippingsParserService
from src.domain.entities import Clipping, Book
from src.domain.value_objects import Title, Author, Location, CreatedAt, Highlight
from unittest.mock import mock_open, patch

def test_parse_to_entities():
    mock_file_content = (
        "Book Title (Author Name)\n"
        "- Your Highlight on page 138 | Location 1780-1784 | Added on Saturday, February 8, 2025 11:39:30 AM\n"
        "This is a highlight.\n"
        "==========\n"
        "Another Book (Another Author)\n"
        "- Your Highlight on page 50 | Location 500-504 | Added on Sunday, March 9, 2025 10:00:00 AM\n"
        "Another highlight.\n"
    )

    parser = ClippingsParserService()

    # Pass the file content directly to the parser
    books = parser.parse_to_entities(mock_file_content)

    assert len(books) == 2

    # Validate first book
    book1 = books[0]
    assert book1.title == Title("Book Title")
    assert book1.author == Author("Author Name")
    assert len(book1.clippings) == 1

    clipping1 = book1.clippings[0]
    assert clipping1.title == Title("Book Title")
    assert clipping1.author == Author("Author Name")
    assert clipping1.location == Location("1780-1784")
    assert clipping1.created_at.value == datetime(2025, 2, 8, 11, 39, 30)
    assert clipping1.highlight == Highlight("This is a highlight.")

    # Validate second book
    book2 = books[1]
    assert book2.title == Title("Another Book")
    assert book2.author == Author("Another Author")
    assert len(book2.clippings) == 1

    clipping2 = book2.clippings[0]
    assert clipping2.title == Title("Another Book")
    assert clipping2.author == Author("Another Author")
    assert clipping2.location == Location("500-504")
    assert clipping2.created_at.value == datetime(2025, 3, 9, 10, 0, 0)
    assert clipping2.highlight == Highlight("Another highlight.")

import pytest
from datetime import datetime
from src.infrastructure.MarkdownBookFormatter import MarkdownBookFormatter
from src.domain.entities import Book, Title, Author, Clipping, Location, Highlight

@pytest.fixture
def sample_book():
    return Book(
        title=Title("Sample Book"),
        author=Author("Sample Author"),
        clippings=[
            Clipping(
                title=Title("Sample Book"),
                author=Author("Sample Author"),
                location=Location("123-124"),
                highlight=Highlight("This is a sample highlight."),
                created_at=datetime(2025, 8, 31, 12, 0, 0)
            ),
            Clipping(
                title=Title("Sample Book"),
                author=Author("Sample Author"),
                location=Location("125-126"),
                highlight=Highlight("Another sample highlight."),
                created_at=datetime(2025, 8, 31, 12, 0, 0)
            )
        ]
    )

def test_markdown_formatter(sample_book):
    formatter = MarkdownBookFormatter()
    markdown_content = formatter.format(sample_book)

    assert "# Sample Book" in markdown_content
    assert "**Author:** Sample Author" in markdown_content
    assert "- **Location 123-124**:" in markdown_content
    assert "This is a sample highlight." in markdown_content
    assert "- **Location 125-126**:" in markdown_content
    assert "Another sample highlight." in markdown_content
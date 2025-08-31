from datetime import datetime
from typing import List
from .entities import Clipping, Book
from .value_objects import Title, Author, Location, CreatedAt, Highlight

class ClippingsParserService:
    """
    A service to parse Kindle clippings from the "My Clippings.txt" file.
    """

    def parse_to_entities(self, file_content: str) -> List[Book]:
        """
        Parse the Kindle clippings content and return domain entities.

        Args:
            file_content (str): The content of the "My Clippings.txt" file as a string.

        Returns:
            List[Book]: A list of Book entities with their associated clippings.
        """
        # Remove BOM if present
        content = file_content.lstrip('\ufeff')

        # Split clippings by delimiter
        entries = content.split("==========")

        books = {}

        for entry in entries:
            lines = [line.strip() for line in entry.strip().split("\n") if line.strip()]
            if len(lines) < 3:
                continue

            title_author = lines[0]
            metadata = lines[1]
            highlight = "\n".join(lines[2:])

            # Extract title and author
            title, author = self._extract_title_author(title_author)

            # Remove BOM from title only
            title = title.lstrip('\ufeff')

            # Extract location and created_at
            location = self._extract_location(metadata)
            created_at = self._extract_created_at(metadata)

            # Create Clipping entity
            clipping = Clipping(
                title=Title(title),
                author=Author(author),
                location=Location(location),
                created_at=created_at,
                highlight=Highlight(highlight)
            )

            # Group clippings by book
            book_key = (title, author)
            if book_key not in books:
                books[book_key] = Book(
                    title=Title(title),
                    author=Author(author),
                    clippings=[]
                )
            books[book_key].clippings.append(clipping)

        return list(books.values())

    def _extract_title_author(self, title_author: str) -> tuple:
        """
        Extract the title and author from the first line of a clipping.

        Args:
            title_author (str): The first line containing title and author.

        Returns:
            tuple: A tuple containing the title and author.
        """
        # Example: "Book Title (Author Name)"
        if "(" in title_author and ")" in title_author:
            title, author = title_author.rsplit("(", 1)
            return title.strip(), author.strip(")")
        return title_author, "Unknown"

    def _extract_location(self, metadata: str) -> str:
        """
        Extract the location from the metadata line.

        Args:
            metadata (str): The second line containing metadata.

        Returns:
            str: The extracted location.
        """
        # Split metadata by "|" and find the part containing "Location"
        parts = metadata.split("|")
        for part in parts:
            if "Location" in part:
                return part.split("Location")[-1].strip()
        return "Unknown"

    def _extract_created_at(self, metadata: str) -> CreatedAt:
        """
        Extract the "Added on" timestamp from the metadata line and pass it to the CreatedAt constructor.

        Args:
            metadata (str): The second line containing metadata.

        Returns:
            CreatedAt: A CreatedAt value object with the parsed timestamp.
        """
        # Split metadata by "|" and find the part containing "Added on"
        parts = metadata.split("|")
        for part in parts:
            if "Added on" in part:
                date_str = part.split("Added on")[-1].strip()
                return CreatedAt(date_str)
        return CreatedAt("Unknown")  # Default to "Unknown" if no date is found

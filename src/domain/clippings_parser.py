import re
from typing import List
from .entities import Clipping, Book
from .value_objects import Title, Author, Location, CreatedAt, Highlight

class ClippingsParser:
    """
    A class to parse Kindle clippings from the "My Clippings.txt" file.
    """

    def parse(self, file_path: str) -> List[Book]:
        """
        Parse the Kindle clippings file and extract highlights, notes, and bookmarks.

        Args:
            file_path (str): Path to the "My Clippings.txt" file.

        Returns:
            List[Book]: A list of Book objects containing parsed clippings.
        """
        clippings = []
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split clippings by delimiter
        entries = content.split("==========")

        for entry in entries:
            lines = [line.strip() for line in entry.strip().split("\n") if line.strip()]
            if len(lines) < 3:
                continue

            title_author = lines[0]
            metadata = lines[1]
            highlight = "\n".join(lines[2:])

            # Extract title and author
            title, author = self._extract_title_author(title_author)

            # Extract location or other metadata
            location = self._extract_location(metadata)

            clippings.append(Clipping(
                title=Title(title),
                author=Author(author),
                location=Location(location),
                created_at=CreatedAt("Unknown"),  # Placeholder for CreatedAt
                highlight=Highlight(highlight)
            ))

        return self._group_by_book(clippings)

    def _extract_title_author(self, title_author: str) -> tuple[str, str]:
        """
        Extract the title and author from the first line of a clipping.

        Args:
            title_author (str): The title and author string.

        Returns:
            tuple[str, str]: A tuple containing the title and author.
        """
        match = re.match(r"^(.*) \((.*)\)$", title_author)
        if match:
            return match.group(1), match.group(2)
        return title_author, "Unknown"

    def _extract_location(self, metadata: str) -> str:
        """
        Extract the location from the metadata line.

        Args:
            metadata (str): The metadata string.

        Returns:
            str: The extracted location.
        """
        match = re.search(r"Location ([0-9-]+)", metadata)
        if match:
            return match.group(1)
        return "Unknown"

    def _group_by_book(self, clippings: List[Clipping]) -> List[Book]:
        """
        Group clippings by book title and author.

        Args:
            clippings (List[Clipping]): List of parsed clippings.

        Returns:
            List[Book]: A list of Book objects.
        """
        grouped = {}
        for clipping in clippings:
            key = (clipping.title.value, clipping.author.value)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(clipping)

        return [
            Book(title=Title(key[0]), author=Author(key[1]), clippings=grouped[key])
            for key in grouped
        ]

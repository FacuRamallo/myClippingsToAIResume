import re
from typing import List
from .entities import Clipping, Book
from .value_objects import Title, Author, Location, CreatedAt, Highlight

class ClippingsParserService:
    """
    A service to parse Kindle clippings from the "My Clippings.txt" file.
    """

    def parse_to_dto(self, file_path: str) -> List[dict]:
        """
        Parse the Kindle clippings file and return raw DTOs.

        Args:
            file_path (str): Path to the "My Clippings.txt" file.

        Returns:
            List[dict]: A list of raw clippings data as dictionaries.
        """
        clippings = []
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()

        # Remove BOM if present
        content = content.lstrip('\ufeff')

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

            # Remove BOM from title only
            title = title.lstrip('\ufeff')

            # Extract location or other metadata
            location = self._extract_location(metadata)

            clippings.append({
                "title": title,
                "author": author,
                "location": location,
                "highlight": highlight
            })
        return clippings

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
        # Example: "- Your Highlight on Location 123-124 | Added on Thursday, January 1, 2022"
        if "Location" in metadata:
            location_part = metadata.split("Location")[-1]
            return location_part.split("|")[0].strip()
        return "Unknown"

from typing import List
from src.domain.entities import Book

class MarkdownBookFormatter:
    """
    A class responsible for formatting book entities into Markdown content.
    """

    def format(self, book: Book) -> str:
        """
        Format a Book entity into Markdown content.

        Args:
            book (Book): The book entity containing title, author, and clippings.

        Returns:
            str: The formatted Markdown content.
        """
        header = f"""# {book.title.value}

**Author:** {book.author.value}

---

"""

        highlights_md = "\n\n".join(
            [
                f"- **Location {clipping.location.value}**:\n{self._format_to_markdown_list(clipping.highlight.value)}"
                for clipping in book.clippings
            ]
        )

        return header + highlights_md

    def _format_to_markdown_list(self, input_text: str) -> str:
        """
        Convert a string with bullet points into a properly indented Markdown list.

        Args:
            input_text (str): The input string containing bullet points.

        Returns:
            str: The formatted Markdown list.
        """
        import re
        bullet_pattern = r"•\s*([^•]+)"
        formatted_text = re.sub(bullet_pattern, r"\n  - \1", input_text)
        return formatted_text
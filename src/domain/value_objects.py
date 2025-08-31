from dataclasses import dataclass
from typing import Any
from datetime import datetime

@dataclass(frozen=True)
class Title:
    value: str

@dataclass(frozen=True)
class Author:
    value: str

@dataclass(frozen=True)
class Location:
    value: str

@dataclass(frozen=True)
class CreatedAt:
    value: datetime

    def __init__(self, date_str: str):
        """
        Initialize the CreatedAt value object by parsing a date string.

        Args:
            date_str (str): The raw date string to parse.

        Raises:
            ValueError: If the date string cannot be parsed.
        """
        object.__setattr__(self, 'value', self._parse_date(date_str))

    def _parse_date(self, date_str: str) -> datetime:
        """
        Parse the date string into a datetime object.

        Args:
            date_str (str): The raw date string to parse.

        Returns:
            datetime: The parsed datetime object.
        """
        return datetime.strptime(date_str, "%A, %B %d, %Y %I:%M:%S %p")

@dataclass(frozen=True)
class Highlight:
    value: str

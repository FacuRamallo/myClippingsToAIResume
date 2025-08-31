from dataclasses import dataclass
from typing import Any

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
    value: str

@dataclass(frozen=True)
class Highlight:
    value: str

from dataclasses import dataclass
from typing import List
from .value_objects import Title, Author, Location, CreatedAt, Highlight

@dataclass(frozen=True)
class Clipping:
    title: Title
    author: Author
    location: Location
    created_at: CreatedAt
    highlight: Highlight

@dataclass(frozen=True)
class Book:
    title: Title
    author: Author
    clippings: List[Clipping]

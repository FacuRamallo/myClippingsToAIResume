# Domain Model

## Entities

### Clipping
**Attributes:**
- Book Title
- Author
- Location
- Highlight Text
- Type (Highlight, Note, Bookmark)

### Book
**Attributes:**
- Title
- Author
- Highlights (List of Clippings)

## Value Objects

### ClippingType
**Description:** Enum representing the type of clipping (Highlight, Note, Bookmark).

## Relationships
- A `Book` contains multiple `Clippings`.
- Each `Clipping` belongs to a single `Book`.

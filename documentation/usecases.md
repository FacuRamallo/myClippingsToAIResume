# Use Cases

## Data Flow

### Use Case 1: Parse Kindle Clippings File
**Description:** Extract highlights, notes, and bookmarks from the `My Clippings.txt` file.

**Actors:** User

**Steps:**
1. User places the `My Clippings.txt` file in the `input files/` directory.
2. The system reads the file and parses its content.
3. Extracted data is grouped by book and stored in memory.

**Data Flow:**
- Input: `My Clippings.txt`
- Process: Parsing and grouping clippings by book.
- Output: Structured data in memory.

### Use Case 2: Generate Per-Book Markdown Files
**Description:** Create Markdown files for each book with metadata and highlights.

**Actors:** User

**Steps:**
1. The system processes the parsed data.
2. For each book, a Markdown file is generated.
3. Files are saved in the `processed_files_output/` directory.

**Data Flow:**
- Input: Parsed data from memory.
- Process: Formatting and writing Markdown files.
- Output: Markdown files in the `processed_files_output/` directory.

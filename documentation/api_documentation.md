# API Documentation

## Overview
This document describes the key functions and methods exposed by the system.

### Application Layer

#### `main.py`
- **Function:** `main()`
  - **Description:** Entry point for the application.
  - **Parameters:** None
  - **Returns:** None

#### `markdown_generator.py`
- **Function:** `generate_markdown(book)`
  - **Description:** Generates a Markdown file for a given book.
  - **Parameters:**
    - `book` (Book): The book object containing metadata and highlights.
  - **Returns:** None

### Domain Layer

#### `clippings_parser.py`
- **Function:** `parse_clippings(file_path)`
  - **Description:** Parses the Kindle clippings file.
  - **Parameters:**
    - `file_path` (str): Path to the `My Clippings.txt` file.
  - **Returns:** List of Clipping objects.

### Infrastructure Layer

#### `local_file_operations.py`
- **Function:** `read_file(file_path)`
  - **Description:** Reads the content of a file.
  - **Parameters:**
    - `file_path` (str): Path to the file.
  - **Returns:** File content as a string.

- **Function:** `write_file(file_path, content)`
  - **Description:** Writes content to a file.
  - **Parameters:**
    - `file_path` (str): Path to the file.
    - `content` (str): Content to write.
  - **Returns:** None

# Infrastructure Diagram

## Overview
The system is designed with a modular architecture, separating the application, domain, and infrastructure layers.

### Layers
1. **Application Layer:**
   - Contains the main entry point and use case logic.
   - Files: `src/application/main.py`, `src/application/markdown_generator.py`

2. **Domain Layer:**
   - Contains the core business logic and domain models.
   - Files: `src/domain/clippings_parser.py`, `src/domain/entities.py`, `src/domain/value_objects.py`

3. **Infrastructure Layer:**
   - Handles file operations and external integrations.
   - Files: `src/infrastructure/file_interfaces.py`, `src/infrastructure/local_file_operations.py`

### Data Flow
1. Input: `My Clippings.txt` file is read by the infrastructure layer.
2. Processing: The domain layer parses and organizes the data.
3. Output: The application layer generates Markdown files and saves them via the infrastructure layer.

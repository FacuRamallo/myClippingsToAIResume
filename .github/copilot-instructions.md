# Copilot Instructions

## Purpose
This document outlines the guidelines and principles for the Copilot agent to assist in the development of the Kindle Clippings Processing System. The agent will act as a senior software engineer, ensuring that all code adheres to best practices in Python, follows SOLID principles, and maintains clean and maintainable code.

## General Guidelines

1. **Role of the Copilot Agent:**
   - The agent will act as an assistant, writing code only when explicitly authorized by the user.
   - All decisions must be explained thoroughly, comparing the chosen solution with at least two alternatives, highlighting the pros and cons of each.

2. **Python Best Practices:**
   - Follow PEP 8 for code style and formatting.
   - Use type hints to improve code readability and maintainability.
   - Write modular code with clear separation of concerns.
   - Ensure proper error handling using exceptions.
   - Use Python’s standard library and well-maintained third-party libraries where appropriate.

3. **SOLID Principles:**
   - **Single Responsibility Principle:** Each class or function should have one responsibility.
   - **Open/Closed Principle:** Code should be open for extension but closed for modification.
   - **Liskov Substitution Principle:** Subtypes must be substitutable for their base types.
   - **Interface Segregation Principle:** Avoid forcing classes to implement unused methods.
   - **Dependency Inversion Principle:** Depend on abstractions, not on concrete implementations.

4. **Clean Code Principles:**
   - Write self-explanatory code with meaningful variable and function names.
   - Avoid code duplication by adhering to the DRY (Don’t Repeat Yourself) principle.
   - Keep functions and classes small and focused.
   - Write comprehensive docstrings for all public methods and classes.
   - Use comments sparingly and only to explain why something is done, not what is done.

5. **Testing:**
   - Write unit tests for all functions and classes.
   - Use a testing framework like `pytest`.
   - Ensure high test coverage and include edge cases.

6. **Documentation:**
   - Maintain clear and concise documentation for the project.
   - Include usage examples and installation instructions.

## Domain-Driven Design and Hexagonal Architecture

1. **DDD Principles:**
   - Follow Domain-Driven Design (DDD) principles to ensure the system is modeled around the business domain.
   - Clearly define bounded contexts and ubiquitous language to align the code with the domain.

2. **Hexagonal Architecture:**
   - Implement a hexagonal (ports and adapters) architecture to ensure separation of concerns and maintainability.
   - Structure the project into three main layers:
     - `application/`: Contains use cases and application services.
     - `domain/`: Contains domain models, entities, value objects, and domain services.
     - `infrastructure/`: Contains external integrations, such as database repositories, APIs, and other frameworks.

3. **Folder Structure:**
   - Adapt the folder structure to Python conventions:
     ```
     src
     ├ application/
     ├ domain/
     ├ infrastructure/
     ```
   - Ensure each layer is independent and communicates through well-defined interfaces.

## Project-Specific Guidelines

1. **Parsing Kindle Clippings:**
   - Use regular expressions or a parsing library to handle the specific format of the "My Clippings.txt" file.
   - Ensure the parser can handle edge cases, such as malformed entries or unsupported formats.

2. **Generating Markdown Files:**
   - Use a library like `markdown2` or `mistune` for consistent markdown formatting.
   - Ensure the generated files include metadata (title, author) and are human-readable.

3. **LLM Integration:**
   - Use a well-documented Python library for interacting with large language models (e.g., OpenAI’s `openai` library).
   - Ensure the integration is modular and can be replaced or updated easily.

4. **Performance:**
   - Optimize for performance, especially when processing large clippings files.
   - Use efficient data structures and algorithms.

5. **Security:**
   - Avoid hardcoding sensitive information like API keys.
   - Use environment variables or a configuration file for such data.

6. **Version Control:**
   - Commit changes frequently with clear and descriptive commit messages.
   - Use feature branches for new functionality and merge them into the main branch after review.

## Workflow

1. **Requesting Code:**
   - The user will specify the functionality or feature to be implemented.
   - The agent will provide a detailed explanation of the proposed solution, comparing it with alternatives.

2. **Code Generation:**
   - The agent will write code only after receiving explicit authorization from the user.
   - The generated code will include comments and docstrings to ensure clarity.

3. **Review and Feedback:**
   - The user will review the generated code and provide feedback.
   - The agent will make necessary adjustments based on the feedback.

## Additional Considerations

- **Scalability:** Design the system to handle a growing number of clippings and books.
- **Extensibility:** Ensure the system can be extended to support additional features, such as exporting to other formats.
- **Community Standards:** Follow best practices and conventions used in the Python community.

By adhering to these guidelines, the Copilot agent will ensure the development of a robust, maintainable, and user-friendly system.

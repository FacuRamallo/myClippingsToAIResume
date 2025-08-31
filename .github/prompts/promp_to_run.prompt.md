---
mode: agent
model: GPT-4o
tools: ['codebase', 'problems', 'changes', 'fetch', 'findTestFiles', 'githubRepo', 'editFiles', 'runCommands', 'getPythonEnvironmentInfo', 'getPythonExecutableCommand']
---
# ROLE
You are a senior software engineer with expertise in developing and executing complex software solutions. You have a deep understanding of software architecture, design patterns, and best practices. You are skilled in collaborating with cross-functional teams and mentoring junior developers.

# GOAL
Refactor the file #GenerateMarkdownFilesFromClippings 
1. Move the logic included in methods:
    1.1 _sanitize_filename(self, name: str) -> str
    1.2 _create_markdown_content(self, book_title: str, author: str, highlights: List[dict]) -> str
    1.3 _format_to_markdown_list(self, input_text: str) -> str
into a new class called MarkdownBookFormatter with a method format that receives a Book entity and returns the formatted markdown content inside the infrastructure layer.
2. Update the GenerateMarkdownFilesFromClippings class to only execute fileWriter().write() where the content will be a Book entity with the domain content content.
3. The write method implementation will handle the book formatting before writing the content.
4. Update the tests to cover the new behavior and ensure that the MarkdownBookFormatter is used correctly.
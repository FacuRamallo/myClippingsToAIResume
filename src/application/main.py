import os
from src.domain.clippings_parser import ClippingsParser
from src.application.markdown_generator import MarkdownGenerator
from dotenv import load_dotenv
from src.domain.entities import Book

# Load environment variables from .env file
load_dotenv()

def generate_markdown_files(clippings_file: str, output_dir: str):
    """
    Parse clippings and generate Markdown files for each book.

    Args:
        clippings_file (str): Path to the "My Clippings.txt" file.
        output_dir (str): Directory to save the Markdown files.
    """
    # Parse clippings
    parser = ClippingsParser()
    books = parser.parse(clippings_file)

    # Initialize Markdown generator
    generator = MarkdownGenerator(output_dir)

    # Generate Markdown files for each book
    for book in books:
        generator.generate_markdown(
            book.title.value,
            book.author.value,
            [
                {
                    "location": clipping.location.value,
                    "highlight": clipping.highlight.value
                }
                for clipping in book.clippings
            ]
        )

def get_env_variable(var_name: str, default: str) -> str:
    """
    Get the value of an environment variable or return a default value.

    Args:
        var_name (str): The name of the environment variable.
        default (str): The default value to return if the variable is not set.

    Returns:
        str: The value of the environment variable or the default value.
    """
    return os.getenv(var_name, default)

if __name__ == "__main__":
    # Configure paths using environment variables
    clippings_file = get_env_variable("CLIPPINGS_FILE", "input_files/My Clippings.txt")
    output_dir = get_env_variable("OUTPUT_DIR", "processed_files_output")

    # Ensure the input and output directories exist
    input_dir = os.path.dirname(clippings_file)
    output_dir_path = os.path.abspath(output_dir)

    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir_path, exist_ok=True)

    if not os.path.exists(clippings_file):
        print(f"Clippings file not found: {clippings_file}")
    else:
        generate_markdown_files(clippings_file, output_dir)
        print(f"Markdown files generated in: {output_dir}")

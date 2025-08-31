import os
from dotenv import load_dotenv
import logging
from src.infrastructure.local_file_operations import LocalFileReader, LocalFileWriter
from application.GenerateMarkdownFilesFromClippings import GenerateMarkdownFilesFromClippings

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
        # Initialize the Markdown generator use case
        file_writer = LocalFileWriter()
        file_reader = LocalFileReader()
        generator = GenerateMarkdownFilesFromClippings(output_dir, clippings_file, file_reader, file_writer)
        generator.execute()
        print(f"Markdown files generated in: {output_dir}")

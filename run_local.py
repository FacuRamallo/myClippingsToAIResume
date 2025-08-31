import os
from src.infrastructure.local_file_operations import LocalFileReader, LocalFileWriter
from src.application.GenerateMarkdownFilesFromClippings import GenerateMarkdownFilesFromClippings

def main():
    """
    Main method to execute the use case.
    """
    # Get environment variables
    input_file = os.getenv("CLIPPINGS_FILE", "input files/My Clippings.txt")
    output_dir = os.getenv("OUTPUT_DIR", "processed_files_output")

    # Ensure the input and output directories exist
    os.makedirs(os.path.dirname(input_file), exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Initialize file reader and writer
    file_reader = LocalFileReader()
    file_writer = LocalFileWriter()

    # Initialize the use case
    use_case = GenerateMarkdownFilesFromClippings(output_dir, input_file, file_reader, file_writer)

    # Execute the use case
    use_case.execute()

if __name__ == "__main__":
    main()

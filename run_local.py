import os
from src.infrastructure.GoogleGenAIClient import GoogleGenAIClient
from src.application.SummaryGenerator import SummaryGenerator
from src.infrastructure.local_file_operations import LocalFileReader, LocalFileWriter
from src.application.GenerateMarkdownFilesFromClippings import GenerateMarkdownFilesFromClippings

def main():
    """
    Main method to execute the use case.
    """
    # Get environment variables
    myClippingsInputFile = os.getenv("CLIPPINGS_FILE", "input_files/parsing/My Clippings.txt")
    bookToResumeDir = os.getenv("BOOK_TO_RESUME_DIR", "input_files/summarizing")
    booksOutputDir = os.getenv("BOOKS_OUTPUT_DIR", "processed_files_output/Books")
    summariesOutputDir = os.getenv("SUMMARIES_OUTPUT_DIR", "processed_files_output/books_summaries")

    # Ensure the input and output directories exist
    os.makedirs(os.path.dirname(myClippingsInputFile), exist_ok=True)
    os.makedirs(bookToResumeDir, exist_ok=True)
    os.makedirs(booksOutputDir, exist_ok=True)
    os.makedirs(summariesOutputDir, exist_ok=True)

    # Initialize file reader and writer
    file_reader = LocalFileReader()
    file_writer = LocalFileWriter()

    # Initialize the use case
    use_case = GenerateMarkdownFilesFromClippings(booksOutputDir, myClippingsInputFile, file_reader, file_writer)

    # Execute the use case
    use_case.execute()

    # Initialize the LLM client
    api_key = os.getenv("GOOGLE_GENAI_API_KEY", "your-api-key")
    llm_client = GoogleGenAIClient(api_key)

    # Initialize the SummaryGenerator use case
    summary_generator = SummaryGenerator(llm_client, bookToResumeDir, summariesOutputDir)

    # Execute the summary generation
    summary_generator.generate_summaries()

if __name__ == "__main__":
    main()

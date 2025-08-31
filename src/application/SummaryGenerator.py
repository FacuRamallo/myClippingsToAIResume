import os
from typing import List
from src.infrastructure.GoogleGenAIClient import GoogleGenAIClient
from src.infrastructure.local_file_operations import LocalFileWriter

class SummaryGenerator:
    """
    Class to handle summary generation from book highlights.
    """

    def __init__(self, llm_client: GoogleGenAIClient, input_dir: str, output_dir: str):
        self.llm_client = llm_client
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.file_writer = LocalFileWriter()

    def generate_summaries(self):
        """
        Generate summaries for all files in the input directory.
        """
        # Check if input directory exists
        if not os.path.exists(self.input_dir):
            print(f"Input directory '{self.input_dir}' does not exist.")
            return

        # Get list of files to summarize
        files_to_summarize = [
            f for f in os.listdir(self.input_dir) if os.path.isfile(os.path.join(self.input_dir, f))
        ]

        if not files_to_summarize:
            print("No files found to summarize.")
            return

        for file_name in files_to_summarize:
            input_file_path = os.path.join(self.input_dir, file_name)
            with open(input_file_path, 'r') as file:
                highlights = file.readlines()

            # Generate the prompt
            prompt = self._create_prompt(highlights)

            # Generate the summary
            try:
                summary = self.llm_client.generate_summary([prompt])
                self._save_summary(file_name, summary)
                print(f"Summary generated and saved for file: {file_name}")
            except Exception as e:
                print(f"Failed to generate summary for file {file_name}: {e}")

    def _create_prompt(self, highlights: List[str]) -> str:
        """
        Create a prompt to set the context for summarization.

        Args:
            highlights (List[str]): List of book highlights.

        Returns:
            str: Generated prompt.
        """
        return (
            "You are an expert book summarizer. Your task is to analyze the following highlights, "
            "understand the topic, identify patterns, draw conclusions, and provide practical "
            "recommendations to make the best use of the book's content. Here are the highlights:\n"
            + "\n".join(highlights)
            + "\nThe output format must be in Markdown Format."
        )

    def _save_summary(self, original_file_name: str, summary: str):
        """
        Save the generated summary to the output directory.

        Args:
            original_file_name (str): Name of the original file.
            summary (str): Generated summary.
        """
        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Define the output file path
        output_file_name = os.path.splitext(original_file_name)[0] + "_summary.txt"
        output_file_path = os.path.join(self.output_dir, output_file_name)

        # Write the summary to the file
        self.file_writer.write(output_file_path, summary)

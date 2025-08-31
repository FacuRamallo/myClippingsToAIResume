import os
from src.application.main import generate_markdown_files

def main():
    # Define input and output paths
    input_file = "input files/My Clippings.txt"
    output_dir = "processed_files_output"

    # Ensure input file exists
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}")
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Run the application
    print("Processing clippings...")
    generate_markdown_files(input_file, output_dir)
    print(f"Clippings processed. Output files are in: {output_dir}")

if __name__ == "__main__":
    main()

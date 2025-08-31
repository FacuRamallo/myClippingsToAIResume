# myClippingsToAIResume

Get a book highlights and resume from your Kindle `My Clippings.txt` file.

## Features
- Parse Kindle clippings to extract book highlights, notes, and bookmarks.
- Generate individual Markdown files for each book with metadata and highlights.
- Organize clippings by book for easy reference.

## Requirements
- Python 3.10+
- Install dependencies using `pip install -r requirements.txt`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/FacuRamallo/myClippingsToAIResume.git
   ```
2. Navigate to the project directory:
   ```bash
   cd myClippingsToAIResume
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your `My Clippings.txt` file in the `input files/` directory.
2. Run the script locally:
   ```bash
   python run_local.py
   ```
3. Processed Markdown files will be saved in the `processed_files_output/` directory.

## Running Tests
To run the tests, use the following command:
```bash
pytest tests/
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

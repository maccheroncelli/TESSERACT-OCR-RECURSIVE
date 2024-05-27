# Tesseract OCR Recursive

This script is designed to perform Optical Character Recognition (OCR) on all PDF files within its directory using Tesseract OCR, and outputs the results to a specified output directory. The script leverages `ocrmypdf` to apply OCR to PDF files, making them searchable and editable.

## Features

- Automatically identifies and processes all PDF files in the script's directory.
- Outputs OCR-processed PDFs to a subdirectory named `output`.
- Utilizes Tesseract OCR for text recognition.

## Requirements

- Python 3.x
- `ocrmypdf`
- Tesseract OCR

## Installation

### Python Dependencies

To install the required Python dependencies, run the following command:

```bash
pip install ocrmypdf
```

### Tesseract OCR

#### Windows

1. Download the Tesseract installer from the [official Tesseract repository](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the installer and follow the instructions.
3. Add Tesseract to your system PATH:
   - Open the Start Menu and search for "Environment Variables".
   - Click on "Edit the system environment variables".
   - In the System Properties window, click on the "Environment Variables..." button.
   - In the Environment Variables window, find the "Path" variable in the "System variables" section and click "Edit...".
   - Click "New" and add the path to the Tesseract executable (e.g., `C:\Program Files\Tesseract-OCR`).
   - Click "OK" to close all windows.

## Usage

1. Place the script in the directory containing the PDF files you want to process.
2. Run the script using Python:

```bash
python Tesseract_OCR_Recursive.py
```

The script will create an `output` directory in the same location and save all OCR-processed PDFs there. It will print messages to the console indicating the success or failure of the OCR process for each file.

import os
import subprocess

# Get the directory of the script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Use the script directory as the PDF directory
pdf_directory = script_directory

# Set the output directory to 'output' in the same directory
output_directory = os.path.join(script_directory, 'output')

# Specify the language for OCR (Tamil)
#ocr_language = 'tam'

# Make sure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all PDF files in the PDF directory
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)
    output_pdf_path = os.path.join(output_directory, pdf_file)

    # Run OCRmyPDF
    process = subprocess.run(['ocrmypdf', pdf_file, output_pdf_path])

    # Check for errors and print the output
    if process.returncode == 0:
        print(f'Successfully OCR\'d {pdf_file}')
    else:
        print(f'Error OCR\'ing {pdf_file}: {process.stderr}')
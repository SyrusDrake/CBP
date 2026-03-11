#! /usr/bin/python3

from zipfile import ZipFile
from pypdf import PdfWriter
from os import listdir, remove, rmdir
import argparse

"""A script that extracts downloaded book chapters by Cambridge University Press and merges them into a single PDF. """

# Set up command-line argument parsing
parser = argparse.ArgumentParser(
    description="A script that extracts downloaded book chapters by Cambridge University Press and merges them into a single PDF.")
parser.add_argument(
    "zip_file", help="The name of the zip file containing the downloaded book chapters.")
parser.add_argument(
    "-o", "--output", help="The name of the output merged PDF file. Default is 'merged.pdf'.", default='merged.pdf')
parser.add_argument("-d", "--directory",
                    help="The directory to extract the files to. Default is 'extracted_files'.", default='extracted_files')
parser.add_argument(
    "-c", "--clean", help="Whether to clean up the extracted files after merging. Default is False.", action='store_true')
parser.add_argument(
    "-z", "--delete-zip", help="Whether to delete the original zip file after processing. Default is False.", action='store_true')
args = parser.parse_args()

# Unzip the file
with ZipFile(args.zip_file, 'r') as zObject:
    zObject.extractall(path=args.directory)

print(f"Extracted files to {args.directory}. Now merging PDFs...")

# Makes a list of all pdf files that were extracted
pdf_files = [f for f in listdir(args.directory) if f.endswith('.pdf')]

pdf_files.sort()  # Sort the PDF files alphabetically
print(f"Found {len(pdf_files)} PDF files: {pdf_files}")

# Merges the pdf files into a single pdf file
merger = PdfWriter()

for pdf in pdf_files:
    merger.append(f'{args.directory}/{pdf}')

merger.write(args.output)
merger.close()

print(f"Merged PDF saved as {args.output}.")

# If flagged, clean up the extracted files and delete the original zip file
if args.clean:
    print(f"Cleaning up extracted files in {args.directory}...")
    for pdf in pdf_files:
        remove(f'{args.directory}/{pdf}')
    rmdir(args.directory)

if args.delete_zip:
    print(f"Deleting original zip file {args.zip_file}...")
    remove(args.zip_file)

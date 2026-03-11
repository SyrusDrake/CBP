# CBP

A script to process downloaded books from Cambridge University Press. It automatically unpacks the downloaded zip files and merges the individual PDF files into a single PDF.

## Usage

Run the script inside the directory containing the downloaded zip files.

Use the following flags:

**"zip_file"**: The name of the zip file containing the downloaded book chapters.

**"-o", "--output"**: The name of the output merged PDF file. Default is 'merged.pdf'.

**"-d", "--directory"**: The directory to extract the files to. Default is 'extracted_files'.

**"-c", "--clean"**: Whether to clean up the extracted files after merging. Default is False.

**"-z", "--delete-zip"**: Whether to delete the original zip file after processing. Default is False.

import os
from PyPDF2 import PdfReader

def count_pages_in_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            return len(pdf_reader.pages)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def count_total_pages(pdf_files):
    total_pages = 0
    for pdf_file in pdf_files:
        total_pages += count_pages_in_pdf(pdf_file)
    return total_pages

def get_pdf_files_from_directory(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
    return pdf_files

if __name__ == "__main__":
    directory = input("Enter the directory path containing PDF files: ")
    pdf_files = get_pdf_files_from_directory(directory)
    
    if not pdf_files:
        print("No PDF files found in the specified directory.")
    else:
        total_pages = count_total_pages(pdf_files)
        print(f"Total number of pages in all PDF files: {total_pages}")

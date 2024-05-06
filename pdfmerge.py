import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

def merge_pdfs(pdf_files, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)

    with open(output_file, 'wb') as output:
        pdf_merger.write(output)

    print("PDFs merged successfully into", output_file)

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    return list(file_paths)

if __name__ == "__main__":
    pdf_files_to_merge = select_files()

    if len(pdf_files_to_merge) < 2:
        print("Error: You must select at least two PDF files to merge.")
    else:
        output_file = input("Enter the name of the output merged PDF file: ")
        if not output_file.endswith('.pdf'):
            output_file += '.pdf'
        merge_pdfs(pdf_files_to_merge, output_file)

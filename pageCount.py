import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader

# Function to count pages in a single PDF file
def count_pages_in_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            return len(pdf_reader.pages)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

# Function to count total pages in a list of PDF files
def count_total_pages(pdf_files):
    total_pages = 0
    for pdf_file in pdf_files:
        total_pages += count_pages_in_pdf(pdf_file)
    return total_pages

# Function to get a list of PDF files from a directory
def get_pdf_files_from_directory(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
    return pdf_files

# Function to handle the directory selection and page counting
def handle_count_pages():
    directory = filedialog.askdirectory(title="Select Directory Containing PDF Files")
    if directory:
        pdf_files = get_pdf_files_from_directory(directory)
        if not pdf_files:
            messagebox.showwarning("No PDFs Found", "No PDF files found in the specified directory.")
        else:
            total_pages = count_total_pages(pdf_files)
            messagebox.showinfo("Total Pages", f"Total number of pages in all PDF files: {total_pages}")

# Create the main window
root = tk.Tk()
root.title("PDF Page Counter")

# Create and place the count pages button
count_button = tk.Button(root, text="Count Pages in PDFs", command=handle_count_pages)
count_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

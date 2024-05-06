import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os

def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def select_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(tk.END, input_file_path)
    set_default_output(input_file_path)

def set_default_output(input_file_path):
    output_directory = os.path.dirname(input_file_path)
    base_name = os.path.basename(input_file_path)
    output_file_path = os.path.join(output_directory, os.path.splitext(base_name)[0] + "_compressed.pdf")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(tk.END, output_file_path)

def compress():
    input_path = input_file_entry.get()
    output_path = output_file_entry.get()

    if input_path and output_path:
        compress_pdf(input_path, output_path)
        status_label.config(text="PDF compression completed successfully.")
    else:
        status_label.config(text="Please select input file.")

# Create the main window
root = tk.Tk()
root.title("PDF Compressor")

# Create input file selection widgets
input_file_label = tk.Label(root, text="Select Input PDF File:")
input_file_label.grid(row=0, column=0, padx=5, pady=5)

input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)

input_file_button = tk.Button(root, text="Browse", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=5, pady=5)

# Create output file entry widgets
output_file_label = tk.Label(root, text="Output PDF File:")
output_file_label.grid(row=1, column=0, padx=5, pady=5)

output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)

# Create compress button
compress_button = tk.Button(root, text="Compress PDF", command=compress)
compress_button.grid(row=2, column=1, padx=5, pady=10)

# Create status label
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=1, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()

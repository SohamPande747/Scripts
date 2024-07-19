import os
import tkinter as tk
from tkinter import filedialog, messagebox
from comtypes import client

# Function to convert a single DOC/DOCX file to PDF
def convert_doc_to_pdf(input_doc, output_pdf):
    word = client.CreateObject("Word.Application")
    word.Visible = False

    try:
        doc = word.Documents.Open(input_doc)
        doc.SaveAs(output_pdf, FileFormat=17)  # 17 represents PDF format
        doc.Close()
    except Exception as e:
        print(f"Error converting {input_doc}: {e}")
    finally:
        word.Quit()

# Function to batch convert DOC/DOCX files to PDF
def batch_convert_docs_to_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx") or filename.endswith(".doc"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            convert_doc_to_pdf(input_path, output_path)

# Function to handle the folder selection and file conversion
def handle_conversion():
    input_folder = filedialog.askdirectory(title="Select Input Folder Containing DOC/DOCX Files")
    output_folder = filedialog.askdirectory(title="Select Output Folder for PDF Files")
    
    if input_folder and output_folder:
        batch_convert_docs_to_pdfs(input_folder, output_folder)
        messagebox.showinfo("Conversion Complete", "All DOC/DOCX files have been converted to PDF.")
    else:
        messagebox.showwarning("Input Required", "Please select both input and output folders.")

# Create the main window
root = tk.Tk()
root.title("DOC to PDF Converter")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert DOC/DOCX to PDF", command=handle_conversion)
convert_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

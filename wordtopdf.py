import os
from comtypes import client

def convert_doc_to_pdf(input_doc, output_pdf):
    word = client.CreateObject("Word.Application")
    word.Visible = True

    doc = word.Documents.Open(input_doc)
    doc.SaveAs(output_pdf, FileFormat=17)  # 17 represents PDF format
    doc.Close()

    word.Quit()

def batch_convert_docs_to_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx") or filename.endswith(".doc"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            convert_doc_to_pdf(input_path, output_path)

# Prompt the user to input the input and output folders
input_folder = input("Enter the input folder path: ")
output_folder = input("Enter the output folder path: ")

# Call the function to batch convert DOC to PDF
batch_convert_docs_to_pdfs(input_folder, output_folder)

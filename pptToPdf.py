import os
import tkinter as tk
from tkinter import filedialog, messagebox
from comtypes import client

# Function to convert a single PPT/PPTX file to PDF
def convert_ppt_to_pdf(input_ppt, output_pdf):
    powerpoint = client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = False

    try:
        ppt = powerpoint.Presentations.Open(input_ppt)
        ppt.SaveAs(output_pdf, 32)  # 32 represents PDF format
        ppt.Close()
    except Exception as e:
        print(f"Error converting {input_ppt}: {e}")
    finally:
        powerpoint.Quit()

# Function to batch convert PPT/PPTX files to PDF
def batch_convert_ppts_to_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pptx") or filename.endswith(".ppt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            convert_ppt_to_pdf(input_path, output_path)

# Function to handle the folder selection and file conversion
def handle_conversion():
    input_folder = filedialog.askdirectory(title="Select Input Folder Containing PPT/PPTX Files")
    output_folder = filedialog.askdirectory(title="Select Output Folder for PDF Files")
    
    if input_folder and output_folder:
        batch_convert_ppts_to_pdfs(input_folder, output_folder)
        messagebox.showinfo("Conversion Complete", "All PPT/PPTX files have been converted to PDF.")
    else:
        messagebox.showwarning("Input Required", "Please select both input and output folders.")

# Create the main window
root = tk.Tk()
root.title("PPT to PDF Converter")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert PPT/PPTX to PDF", command=handle_conversion)
convert_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

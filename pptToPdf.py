# script to convert ppt into pdf

import os
from comtypes import client


def convert_ppt_to_pdf(input_ppt, output_pdf):
    powerpoint = client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = True

    ppt = powerpoint.Presentations.Open(input_ppt)
    ppt.SaveAs(output_pdf, 32)  # 32 represents PDF format
    ppt.Close()

    powerpoint.Quit()


def batch_convert_ppts_to_pdfs(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pptx") or filename.endswith(".ppt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".pdf")
            convert_ppt_to_pdf(input_path, output_path)


# Prompt the user to input the input and output folders
input_folder = input("Enter the input folder path: ")
output_folder = input("Enter the output folder path: ")

# Call the function to batch convert PPT to PDF
batch_convert_ppts_to_pdfs(input_folder, output_folder)

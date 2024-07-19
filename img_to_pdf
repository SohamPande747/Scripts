import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF

# Function to select images and add to list
def select_images():
    files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    for file in files:
        if file not in selected_images:
            selected_images.append(file)
            listbox.insert(tk.END, os.path.basename(file))

# Function to remove selected image from list
def remove_selected_image():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        del selected_images[index]

# Function to create PDF from selected images
def create_pdf():
    if not selected_images:
        messagebox.showerror("Error", "No images selected")
        return
    
    pdf = FPDF()
    for image_path in selected_images:
        image = Image.open(image_path)
        image_width, image_height = image.size
        pdf.add_page()
        pdf.image(image_path, 0, 0, pdf.w, pdf.h * (image_height / image_width))
    
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if save_path:
        pdf.output(save_path)
        messagebox.showinfo("Success", f"PDF saved successfully at {save_path}")

# Initialize main window
root = tk.Tk()
root.title("Image to PDF Converter")

selected_images = []

# Frame for listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Listbox to display selected images
listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=50, height=15)
listbox.pack(side=tk.LEFT, padx=(0, 10))

# Scrollbar for listbox
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Buttons for selecting, removing, and creating PDF
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

select_button = tk.Button(button_frame, text="Select Images", command=select_images)
select_button.pack(side=tk.LEFT, padx=10)

remove_button = tk.Button(button_frame, text="Remove Selected Image", command=remove_selected_image)
remove_button.pack(side=tk.LEFT, padx=10)

create_pdf_button = tk.Button(button_frame, text="Create PDF", command=create_pdf)
create_pdf_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
root.mainloop()

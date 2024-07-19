import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pydub import AudioSegment

# Function to convert a single file to MP3
def convert_to_mp3(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format="mp3")
        print(f"Converted {input_file} to {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Function to batch convert files to MP3
def batch_convert_to_mp3(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".webm"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".webm", ".mp3"))
            if not convert_to_mp3(input_file, output_file):
                return False
    return True

# Function to handle the conversion process
def handle_conversion():
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    
    if input_folder and output_folder:
        success = batch_convert_to_mp3(input_folder, output_folder)
        if success:
            messagebox.showinfo("Success", "All files have been converted successfully!")
        else:
            messagebox.showerror("Error", "An error occurred during the conversion.")
    else:
        messagebox.showwarning("Input Required", "Please select both input and output folders.")

# Create the main window
root = tk.Tk()
root.title("Audio Converter")

# Create and place the convert button
convert_button = tk.Button(root, text="Convert WebM to MP3", command=handle_conversion)
convert_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

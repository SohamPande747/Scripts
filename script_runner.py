import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess

# Function to run the script and display output
def run_script(script_path):
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")

# List of script paths
scripts = [
    "img_to_pdf.py",
    "mp3_convert.py",
    "pageCount.py",
    "pdfCompress.py",
    "pdfmerge.py",
    "pptToPdf.py",
    "wordtopdf.py",
    "videoDownload.py"
]

# Create the main window
root = tk.Tk()
root.title("Python Script Runner")
root.geometry("800x600")
root.configure(bg='#F9F9F9')  # Light gray background

# Apply a theme to the GUI
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                background="#FF0000",
                foreground="white",
                font=("Arial", 10, "bold"))
style.map("TButton",
          background=[('active', '#CC0000')])

# Create a top frame for the title and buttons
top_frame = ttk.Frame(root, padding="10")
top_frame.pack(side=tk.TOP, fill=tk.X)

# Add a title label
title_label = ttk.Label(top_frame, text="Python Script Runner", font=("Arial", 16, "bold"), foreground="#333")
title_label.pack(pady=(0, 10))

# Create a frame for the buttons
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(side=tk.TOP, fill=tk.X)

# Create buttons for each script
for script in scripts:
    button = ttk.Button(button_frame, text=script, command=lambda s=script: run_script(s))
    button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a scrolled text area to display script output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=25, font=("Arial", 10))
output_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Add a label for the output area
output_label = ttk.Label(root, text="Script Output", font=("Arial", 12, "bold"), foreground="#333")
output_label.pack(pady=(0, 5))

# Run the Tkinter event loop
root.mainloop()

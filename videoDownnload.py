import tkinter as tk
from tkinter import messagebox
import yt_dlp

# Function to download playlist
def download_playlist(playlist_url):
    try:
        options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': None,  # Skip merging
            'noplaylist': False,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([playlist_url])

        print("Download complete!")
        messagebox.showinfo("Success", "Download complete!")
    except yt_dlp.DownloadError as e:
        for err in e.exc_info:
            if isinstance(err, yt_dlp.utils.ExtractorError) and 'unavailable' in str(err):
                print("Skipped unavailable audio.")
                messagebox.showwarning("Warning", "Skipped unavailable audio.")
            else:
                print(f"An error occurred: {err}")
                messagebox.showerror("Error", f"An error occurred: {err}")

# Function to handle the button click
def handle_download():
    playlist_url = url_entry.get()
    if playlist_url:
        download_playlist(playlist_url)
    else:
        messagebox.showwarning("Input Required", "Please enter a playlist URL.")

# Create the main window
root = tk.Tk()
root.title("YouTube Playlist Downloader")

# Create and place the URL entry
tk.Label(root, text="Enter Playlist URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download Playlist", command=handle_download)
download_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

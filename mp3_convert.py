import os
from pydub import AudioSegment

def convert_to_mp3(input_file, output_file):
    # Load audio file
    audio = AudioSegment.from_file(input_file)
    
    # Export audio in MP3 format
    audio.export(output_file, format="mp3")
    print(f"Converted {input_file} to {output_file}")

def batch_convert_to_mp3(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):  # Adjust the file extension as needed
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".wav", ".mp3")) # Change file extension
            convert_to_mp3(input_file, output_file)

# Example usage
input_folder = input("Enter folder: ")
output_folder = input("Enter folder: ")
batch_convert_to_mp3(input_folder, output_folder)

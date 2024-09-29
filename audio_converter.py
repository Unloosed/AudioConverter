import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Supported audio formats
supported_formats = ["wav", "mp3", "ogg", "flac", "aac"]

# Welcome message
print("Welcome to the Audio Converter!\n")

# Define the folder containing audio files
FOLDER_PATH = input("Please enter the full path for the folder that contains your audio files: ")

# Get user input for the input and output formats
print("Supported formats: wav, mp3, ogg, flac, aac")
input_format = input("Enter the input audio format (e.g., wav): ").strip().lower()
output_format = input("Enter the output audio format (e.g., mp3): ").strip().lower()

# Check if the formats are supported
if input_format not in supported_formats or output_format not in supported_formats:
    print("Unsupported format. Please choose from the supported formats.")
else:
    # Loop through all files in the folder
    for filename in os.listdir(FOLDER_PATH):
        if filename.endswith(f".{input_format}"):
            try:
                # Construct full file path
                input_file = os.path.join(FOLDER_PATH, filename)
                # Load the input file
                audio = AudioSegment.from_file(input_file, format=input_format)
                # Define the output file path
                output_file = os.path.join(FOLDER_PATH, os.path.splitext(filename)[0] + f".{output_format}")
                # Export as the chosen output format
                audio.export(output_file, format=output_format)
                print(f"Converted {input_file} to {output_file}")
            except CouldntDecodeError:
                print(f"Could not decode {input_file}. Skipping...")
            except Exception as e:
                print(f"An error occurred with {input_file}: {e}")

    print("Conversion complete!")

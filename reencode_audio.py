import os
import ffmpeg

# Supported audio formats
supported_formats = ["wav", "mp3", "ogg", "flac", "aac"]

# Welcome message
print("Welcome to the Audio Re-Encoder!\n")

# Define the folder containing audio files
FOLDER_PATH = input("Please enter the full path for the folder that contains your audio files: ")

# Get user input for the input and output formats
print("Supported formats: wav, mp3, ogg, flac, aac")
input_format = input("Enter the input audio format (e.g., wav): ").strip().lower()
output_format = input("Enter the output audio format (e.g., wav): ").strip().lower()

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
                output_file = os.path.join(FOLDER_PATH, "reencoded_" + os.path.splitext(filename)[0] + f".{output_format}")
                # Re-encode the audio file
                ffmpeg.input(input_file).output(output_file, acodec='pcm_s16le').run()
                print(f"Re-encoded {input_file} to {output_file}")
            except ffmpeg.Error as e:
                print(f"Could not re-encode {input_file}. Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred with {input_file}: {e}")

    print("Re-encoding complete!")

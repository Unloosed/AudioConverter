import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Supported audio formats
SUPPORTED_FORMATS = ["wav", "mp3", "ogg", "flac", "aac"]

def convert_audio(folder_path, input_format, output_format):
    """
    Converts audio files from one format to another within a specified folder.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(f".{input_format}"):
            try:
                input_file = os.path.join(folder_path, filename)
                audio = AudioSegment.from_file(input_file, format=input_format)
                output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + f".{output_format}")
                audio.export(output_file, format=output_format)
                print(f"Converted {input_file} to {output_file}")
            except CouldntDecodeError:
                print(f"Could not decode {input_file}. Skipping...")
            except Exception as e:
                print(f"An error occurred with {input_file}: {e}")

def reencode_audio(folder_path, input_format, output_format):
    """
    Re-encodes audio files by adding a 'reencoded_' prefix to the output filenames.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(f".{input_format}"):
            try:
                input_file = os.path.join(folder_path, filename)
                audio = AudioSegment.from_file(input_file, format=input_format)
                output_file = os.path.join(folder_path, "reencoded_" + os.path.splitext(filename)[0] + f".{output_format}")
                audio.export(output_file, format=output_format)
                print(f"Re-encoded {input_file} to {output_file}")
            except CouldntDecodeError:
                print(f"Could not decode {input_file}. Skipping...")
            except Exception as e:
                print(f"An error occurred with {input_file}: {e}")

def revert_reencode_name(folder_path):
    """
    Reverts filenames by removing the 'reencoded_' prefix.
    """
    for filename in os.listdir(folder_path):
        if filename.startswith("reencoded_"):
            new_filename = filename[len("reencoded_"):]
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")

def main():
    print("Welcome to the Audio Processor!\n")
    print("This tool provides the following functionalities:")
    print("1. Convert audio files from one format to another.")
    print("2. Re-encode audio files by adding a 'reencoded_' prefix to the output filenames.")
    print("3. Revert filenames by removing the 'reencoded_' prefix.\n")

    folder_path = input("Please enter the full path for the folder that contains your audio files: ")
    print(f"Folder path entered: {folder_path}")

    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please enter a valid directory.")
        return

    while True:
        print("Supported formats: wav, mp3, ogg, flac, aac")
        input_format = input("Enter the input audio format (e.g., wav): ").strip().lower()
        output_format = input("Enter the output audio format (e.g., mp3): ").strip().lower()

        if input_format not in SUPPORTED_FORMATS or output_format not in SUPPORTED_FORMATS:
            print("Unsupported format. Please choose from the supported formats.")
            continue

        action = input("Do you want to (1) Convert, (2) Re-encode, or (3) Revert re-encoded filenames? Enter 1, 2, or 3: ").strip()
        if action == '1':
            convert_audio(folder_path, input_format, output_format)
            print("Conversion complete!\n")
        elif action == '2':
            reencode_audio(folder_path, input_format, output_format)
            print("Re-encoding complete!\n")
        elif action == '3':
            revert_reencode_name(folder_path)
            print("Renaming complete!\n")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        another_action = input("Do you want to perform another action? (yes/no): ").strip().lower()
        if another_action != 'yes':
            print("Thank you for using the Audio Processor! Goodbye!")
            break

if __name__ == "__main__":
    main()

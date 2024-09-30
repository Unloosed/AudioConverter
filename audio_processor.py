import os
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Supported audio formats
SUPPORTED_FORMATS = ["wav", "mp3", "ogg", "flac", "aac"]

# Messages
WELCOME_MSG = "Welcome to the Audio Processor!\n"
FUNCTIONALITIES_MSG = (
    "This tool provides the following functionalities:\n"
    "1. Convert audio files from one format to another.\n"
    "2. Re-encode audio files and add a 'reencoded_' prefix to the output filenames.\n"
    "3. Revert filenames by removing the 'reencoded_' prefix.\n"
)
SUPPORTED_FORMATS_MSG = "Supported formats: wav, mp3, ogg, flac, aac"
INVALID_FOLDER_MSG = "Invalid folder path. Please enter a valid directory."
UNSUPPORTED_FORMAT_MSG = "Unsupported format. Please choose from the supported formats."
INVALID_CHOICE_MSG = "Invalid choice. Please enter 1, 2, or 3."
THANK_YOU_MSG = "Thank you for using the Audio Processor! Goodbye!"

def convert_audio(folder_path, input_format, output_format):
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
    for filename in os.listdir(folder_path):
        if filename.startswith("reencoded_"):
            new_filename = filename[len("reencoded_"):]
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)

            # Check if the new file already exists
            if os.path.exists(new_file):
                print(f"Cannot rename {old_file} to {new_file} because the target file already exists. Skipping...")
            else:
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} to {new_file}")


def get_folder_path():
    folder_path = input("Please enter the full path for the folder that contains your audio files: ")
    if not os.path.isdir(folder_path):
        print(INVALID_FOLDER_MSG)
        return None
    return folder_path

def get_audio_formats():
    print(SUPPORTED_FORMATS_MSG)
    input_format = input("Enter the input audio format (e.g., wav): ").strip().lower()
    output_format = input("Enter the output audio format (e.g., mp3): ").strip().lower()
    if input_format not in SUPPORTED_FORMATS or output_format not in SUPPORTED_FORMATS:
        print(UNSUPPORTED_FORMAT_MSG)
        return None, None
    return input_format, output_format

def main():
    print(WELCOME_MSG)
    print(FUNCTIONALITIES_MSG)

    folder_path = get_folder_path()
    if not folder_path:
        return

    while True:
        input_format, output_format = get_audio_formats()
        if not input_format or not output_format:
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
            print(INVALID_CHOICE_MSG)
            continue

        another_action = input("Do you want to perform another action? (y/n): ").strip().lower()
        if another_action != 'y':
            print(THANK_YOU_MSG)
            break

if __name__ == "__main__":
    main()

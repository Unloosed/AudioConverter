# Audio Processor

Welcome to the Audio Processor! This tool allows you to convert and re-encode audio files in various formats. It also provides functionality to revert re-encoded filenames.

## Supported Formats

- WAV
- MP3
- OGG
- FLAC
- AAC

## Functionalities

1. Convert audio files from one format to another.
2. Re-encode audio files and add a `reencoded_` prefix to the output filenames.
3. Revert filenames by removing the `reencoded_` prefix.

## Usage

### Prerequisites

Make sure you have the following Python packages installed:

```bash
pip install pydub
```
### Running the Script
1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using Python:

```bash
python audio_processor.py
```

### Instructions
1. When prompted, enter the full path to the folder containing your audio files.
2. Choose the input and output audio formats from the supported formats.
3. Select the desired action:
   - Enter `1` to convert audio files.
   - Enter `2` to re-encode audio files.
   - Enter `3` to revert re-encoded filenames.
4. Follow the prompts to complete the action.

## Example

```
Welcome to the Audio Processor!

This tool provides the following functionalities:
1. Convert audio files from one format to another.
2. Re-encode audio files and add a 'reencoded_' prefix to the output filenames.
3. Revert filenames by removing the 'reencoded_' prefix.

Please enter the full path for the folder that contains your audio files: /path/to/your/folder
Supported formats: wav, mp3, ogg, flac, aac
Enter the input audio format (e.g., wav): wav
Enter the output audio format (e.g., mp3): mp3
Do you want to (1) Convert, (2) Re-encode, or (3) Revert re-encoded filenames? Enter 1, 2, or 3: 1
Converted /path/to/your/folder/file.wav to /path/to/your/folder/file.mp3
...
Conversion complete!

Do you want to perform another action? (yes/no): no
Thank you for using the Audio Processor! Goodbye!
```

## Error Handling
- If the folder path is invalid, you will be prompted to enter a valid directory.
- If the input or output format is unsupported, you will be prompted to choose from the supported formats.
- If a file cannot be decoded, it will be skipped with an appropriate message.
- If a file with the target name already exists during renaming, the operation will be skipped with an appropriate message.

## GUI
This project also has a GUI implementation. This can be found in `audio_processor_gui.py`

## License

This project is licensed under the MIT License. See the [LICENSE.txt](https://github.com/Unloosed/AudioConverter/tree/main?tab=MIT-1-ov-file) file for details.

## Acknowledgements

Thanks to the developers of the ffmpeg Python library for making audio re-encoding easy. Also thanks to the developers of the pydub library for making the audio conversions possible. Also also thanks to the creators of ffmpeg for the amazing tool :)

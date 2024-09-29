# Audio Processing Scripts

Welcome to AudioConverter! This repository contains two Python scripts for audio file conversion and re-encoding.

## Scripts

1. audio_converter.py
2. re-encode_audio_files.py

## Requirements

See the [requirements.txt](https://github.com/Unloosed/AudioConverter/blob/main/requirements.txt) file for details.

- Python 3.x
- `pydub` library
- `ffmpeg-python` library (for re-encoding script)
- `ffmpeg` installed and accessible from your system's PATH. (Optional)

## Installation

1. Install the required Python libraries:
   ```sh
   pip install pydub ffmpeg-python
   ```
2. Download and install ffmpeg from [ffmpeg.org](https://ffmpeg.org/). (Optional)

## audio_converter.py

This script converts audio files from one format to another.

### Supported Formats

- wav
- mp3
- ogg
- flac
- aac

### Usage

1. Run the script
   ```sh
   python audio_converter.py
   ```
2. Follow the prompts to enter the folder path and the input/output audio formats.

### Example

```
Welcome to the Audio Converter!

Please enter the full path for the folder that contains your audio files: /path/to/your/folder
Supported formats: wav, mp3, ogg, flac, aac
Enter the input audio format (e.g., wav): wav
Enter the output audio format (e.g., mp3): mp3
```
## re-encode_audio_files.py

This script re-encodes audio files from one format to another (or to the same format).

### Supported Formats

- wav
- mp3
- ogg
- flac
- aac

### Usage

1. Run the script
   ```sh
   python re-encode_audio_files.py
   ```
2. Follow the prompts to enter the folder path and the input/output audio formats.

### Example

```
Welcome to the Audio Re-Encoder!

Please enter the full path for the folder that contains your audio files: /path/to/your/folder
Supported formats: wav, mp3, ogg, flac, aac
Enter the input audio format (e.g., wav): wav
Enter the output audio format (e.g., mp3): mp3
```

## Error Handling

Both scripts include error handling to manage files that cannot be decoded or re-encoded and other potential issues. If an error occurs, the script will skip the problematic file and continue processing the rest.

## License

This project is licensed under the MIT License. See the [LICENSE.txt](https://github.com/Unloosed/AudioConverter/tree/main?tab=MIT-1-ov-file) file for details.

## Acknowledgements

Thanks to the developers of the ffmpeg Python library for making audio re-encoding easy. Also thanks to the developers of the pydub library for making the audio conversions possible. Also also thanks to the creators of ffmpeg for the amazing tool :)

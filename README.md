# Audio Processing Scripts

Welcome to the Audio Processing Scripts repository! This repository contains two Python scripts for audio file conversion and re-encoding.

## Scripts

1. audio_converter.py
2. re-encode_audio_files.py

## Requirements

- Python 3.x
- `pydub` library
- `ffmpeg` installed and accessible from your system's PATH
- `ffmpeg-python` library (for re-encoding script)

## Installation

1. Install the required Python libraries:
   ```sh
   pip install pydub ffmpeg-python
   ```
2. Download and install ffmpeg from [ffmpeg.org](https://ffmpeg.org/).

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

```bash
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

```bash
Welcome to the Audio Re-Encoder!

Please enter the full path for the folder that contains your audio files: /path/to/your/folder
Supported formats: wav, mp3, ogg, flac, aac
Enter the input audio format (e.g., wav): wav
Enter the output audio format (e.g., mp3): mp3
```

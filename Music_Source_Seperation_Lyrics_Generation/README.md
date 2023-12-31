# Music Source Separation & Lyrics Generation

## Overview
Music Source Separation & Lyrics Generation is a Python tool designed to process audio files by separating the music components and generating lyrics from the vocal tracks. It utilizes the power of `spleeter` for source separation and an `auto_subtitle` module for transcribing the lyrics. This tool is particularly useful for musicians, producers, and anyone interested in extracting and analyzing lyrics from songs.

## Features
- **Source Separation**: Splits an audio file into different components (like vocals, drums, bass, etc.) using `spleeter`.
- **Lyrics Generation**: Transcribes the vocal component into text, extracting the song's lyrics.
- **Language Support**: Ability to specify the language for accurate transcription of lyrics.
- **Customizable Output**: Generates raw lyrics text and optionally subtitle files with timestamps.

## Requirements
- Python 3.x
- `spleeter`
- `auto_subtitle` (Ensure it supports the required languages)
- ffmpeg (for audio processing by `spleeter`)

## Installation
1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have `ffmpeg` installed on your system. If not, install it from [FFmpeg Official Site](https://ffmpeg.org/download.html).

## Usage
To use the Music Source Separation & Lyrics Generation tool, follow these steps:

1. **Prepare the Audio File**: Place the audio file (e.g., `song.mp3`) in the `input` directory.

2. **Run the Script**: Use the following command format to run the script:
   ```bash
   python main.py --name <audio_file_name> [--language <language_code>]
   ```
   - `<audio_file_name>`: Name of the audio file in the `input` directory (e.g., `song.mp3`).
   - `<language_code>`: (Optional) Language code for lyrics transcription (e.g., `en` for English, `kn` for Kannada). Default is `auto`.

3. **View the Output**: The script generates the lyrics in the `audio_output` directory. You will find the raw lyrics text and, optionally, a subtitle file with timestamps.

## Supported Languages
The tool supports multiple languages for lyrics transcription. Some of the languages include English (en), Spanish (es), German (de), French (fr), and many more. Refer to the `auto_subtitle` documentation for a complete list.

## Customization
You can customize the behavior of the script by modifying the source code, such as changing the `spleeter` model or adjusting the output file formats.

## Contributions
- Tarun Venkat Putturu
- Ruchitha Kuthethoor
- Suhas Somashekar

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- `spleeter` for the source separation functionality.
- The `auto_subtitle` team for the transcription capabilities.

---

For more information, queries, or support, please open an issue in the project's GitHub repository.
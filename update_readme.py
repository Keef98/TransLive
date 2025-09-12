#!/usr/bin/env python3

readme_content = """# Live_trans 🎤🔁🔊

A real-time live translation application that captures audio input, transcribes speech using Whisper AI, translates text from English to French using Argos Translate, and outputs the translation as speech using Text-to-Speech (TTS).

## 🌟 Features

- **Real-time Audio Processing**: Continuous audio capture with silence detection
- **Speech Recognition**: Powered by OpenAI's Whisper AI for accurate speech-to-text conversion
- **Offline Translation**: Uses Argos Translate for English-to-French translation without internet dependency
- **Text-to-Speech**: Converts translated text to natural-sounding speech
- **Transcript Logging**: Automatically saves all translations to a transcript file
- **Cross-platform Support**: Works on macOS, Linux, and Windows
- **Audio Filtering**: Intelligent filtering to remove non-English words and repetitions
- **Customizable Audio Settings**: Configurable input/output devices and sensitivity settings

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Audio input device (microphone)
- Audio output device (speakers/headphones)
- FFmpeg (for audio playback on macOS)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Live_trans
   ```

2. **Install Python dependencies**
   ```bash
   pip install whisper argostranslate TTS sounddevice scipy numpy nltk
   ```

3. **Download NLTK data**
   ```bash
   python -c "import nltk; nltk.download('words')"
   ```

4. **Install Argos Translate model**
   - Download the English-to-French translation model (`en_fr.argosmodel`)
   - Place it in the project root directory

5. **Install FFmpeg** (macOS)
   ```bash
   brew install ffmpeg
   ```

### Usage

1. **Configure audio devices** (optional)
   - Edit `app.py` and modify `INPUT_DEVICE` and `OUTPUT_DEVICE` variables
   - Run `python -c "import sounddevice as sd; print(sd.query_devices())"` to list available devices

2. **Run the application**
   ```bash
   python app.py
   ```

3. **Start speaking**
   - The application will automatically detect speech
   - Wait for the pause detection (1.5 seconds of silence)
   - Your speech will be transcribed, translated, and spoken back

## 📁 Project Structure

```
Live_trans/
├── app.py                    # Main application file
├── README.md                 # This file
├── LICENSE                   # MIT License
├── en_fr.argosmodel         # Translation model (download separately)
├── translation_transcript.txt # Generated transcript log
├── input_audio.wav          # Temporary audio file
├── output.wav               # Generated TTS audio file
└── argostranslate.app/      # Argos Translate application files
```

## ⚙️ Configuration

### Audio Settings

```python
INPUT_DEVICE = 1          # Microphone device index
OUTPUT_DEVICE = 2         # Speaker device index
SILENCE_THRESHOLD = 50    # Audio sensitivity (lower = more sensitive)
PAUSE_TIME = 1.5          # Pause detection time in seconds
```

### Supported Languages

- **Input**: English (configured in Whisper)
- **Output**: French (configurable in Argos Translate)

## 🔧 Technical Details

### Dependencies

- **whisper**: OpenAI's speech recognition model
- **argostranslate**: Offline translation engine
- **TTS**: Text-to-speech synthesis
- **sounddevice**: Real-time audio I/O
- **scipy**: Audio processing
- **numpy**: Numerical operations
- **nltk**: Natural language processing for word filtering

### Audio Processing Pipeline

1. **Audio Capture**: Continuous recording from configured input device
2. **Silence Detection**: Monitors audio levels to detect speech pauses
3. **Speech Recognition**: Converts audio to text using Whisper AI
4. **Text Filtering**: Removes repetitions and non-English words
5. **Translation**: Translates text using Argos Translate
6. **Text-to-Speech**: Converts translated text to audio
7. **Transcript Logging**: Saves all interactions to file

### Performance Considerations

- Uses Whisper's "tiny" model for faster processing
- Single-threaded audio processing for real-time performance
- Configurable silence detection to balance responsiveness and accuracy
- Audio buffering to handle continuous input streams

## 🐛 Troubleshooting

### Common Issues

1. **Audio device not found**
   - Check device indices with `python -c "import sounddevice as sd; print(sd.query_devices())"`
   - Update `INPUT_DEVICE` and `OUTPUT_DEVICE` in `app.py`

2. **Translation model missing**
   - Ensure `en_fr.argosmodel` is in the project root
   - Download from Argos Translate model repository

3. **NLTK data not found**
   - Run `python -c "import nltk; nltk.download('words')"`
   - Check NLTK data path configuration

4. **Audio playback issues**
   - Install FFmpeg: `brew install ffmpeg` (macOS)
   - Check audio output device configuration

### Debug Mode

Enable verbose logging by modifying the print statements in the code or adding logging configuration.

## 📝 Transcript Logging

All translations are automatically saved to `translation_transcript.txt` with timestamps:

```
🎤 Live Translation Transcript
==================================================
[2025-02-20 10:19:30] 🗣️ Input (English): Hello world
[2025-02-20 10:19:30] 🔁 Output (French): Bonjour le monde
--------------------------------------------------
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for speech recognition
- [Argos Translate](https://github.com/argosopentech/argos-translate) for offline translation
- [TTS](https://github.com/coqui-ai/TTS) for text-to-speech synthesis
- [SoundDevice](https://github.com/spatialaudio/python-sounddevice) for audio I/O

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information about your problem

---

**Made with ❤️ for real-time communication across languages**"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("README.md updated successfully!")

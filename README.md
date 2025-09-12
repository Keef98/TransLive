# TransLive 🎤🔁🔊

A sophisticated real-time live translation application that captures audio input, transcribes speech using OpenAI's Whisper AI, translates text from English to French using Argos Translate, and outputs the translation as natural-sounding speech using Text-to-Speech (TTS). This application works completely offline once set up, making it perfect for privacy-conscious users and environments without internet connectivity.

## 🌟 Features

- **Real-time Audio Processing**: Continuous audio capture with intelligent silence detection and pause-based processing
- **Advanced Speech Recognition**: Powered by OpenAI's Whisper AI for highly accurate speech-to-text conversion
- **Offline Translation**: Uses Argos Translate for English-to-French translation without internet dependency
- **Natural Text-to-Speech**: Converts translated text to natural-sounding speech using VCTK voice models
- **Intelligent Audio Filtering**: Advanced filtering to remove non-English words, repetitions, and noise
- **Transcript Logging**: Automatically saves all translations with timestamps to a persistent transcript file
- **Cross-platform Support**: Works seamlessly on macOS, Linux, and Windows
- **Customizable Audio Settings**: Configurable input/output devices, sensitivity settings, and audio parameters
- **Bluetooth Audio Support**: Includes utilities for capturing audio from Bluetooth microphones
- **Thread-safe Processing**: Multi-threaded architecture for smooth real-time performance

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- macOS, Linux, or Windows
- Microphone and speakers/headphones
- At least 4GB RAM (8GB recommended for optimal performance)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TransLive
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv live_tans
   source live_tans/bin/activate  # On Windows: live_tans\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```bash
   python -c "import nltk; nltk.download('words')"
   ```

5. **Configure audio devices**
   - Run `python list_div.py` to list available audio devices
   - Update `INPUT_DEVICE` and `OUTPUT_DEVICE` in `app.py` with your preferred devices

6. **Run the application**
   ```bash
   python app.py
   ```

## 📋 Dependencies

### Core Libraries
- **whisper**: OpenAI's speech recognition model
- **argostranslate**: Offline translation engine
- **TTS**: Text-to-speech synthesis
- **sounddevice**: Real-time audio I/O
- **scipy**: Audio processing and analysis
- **numpy**: Numerical computations
- **nltk**: Natural language processing
- **pyaudio**: Audio capture utilities

### System Requirements
- **macOS**: FFmpeg for audio playback
- **Linux**: ALSA utilities for audio output
- **Windows**: Built-in audio support

## 🛠️ Troubleshooting

### Common Issues

**Audio Device Not Found**
- Run `python list_div.py` to list available devices
- Update device indices in `app.py`
- Ensure microphone permissions are granted

**Tran


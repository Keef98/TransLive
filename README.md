TransLive 🎤🔁🔊

A sophisticated real-time live translation application that captures audio input, transcribes speech using OpenAI's Whisper AI, translates text from English to French using Argos Translate, and outputs the translation as natural-sounding speech using Text-to-Speech (TTS). This application works completely offline once set up, making it perfect for privacy-conscious users and environments without internet connectivity.

🌟 Features

· Real-time Audio Processing: Continuous audio capture with intelligent silence detection and pause-based processing
· Advanced Speech Recognition: Powered by OpenAI's Whisper AI for highly accurate speech-to-text conversion
· Offline Translation: Uses Argos Translate for English-to-French translation without internet dependency
· Natural Text-to-Speech: Converts translated text to natural-sounding speech using VCTK voice models
· Intelligent Audio Filtering: Advanced filtering to remove non-English words, repetitions, and noise
· Transcript Logging: Automatically saves all translations with timestamps to a persistent transcript file
· Cross-platform Support: Works seamlessly on macOS, Linux, and Windows
· Customizable Audio Settings: Configurable input/output devices, sensitivity settings, and audio parameters
· Bluetooth Audio Support: Includes utilities for capturing audio from Bluetooth microphones
· Thread-safe Processing: Multi-threaded architecture for smooth real-time performance
· Error Handling & Recovery: Comprehensive error handling with automatic retry mechanisms
· Performance Monitoring: Real-time monitoring of processing latency and resource usage
· Configuration Management: Flexible configuration system with environment variable support

🚀 Quick Start

Prerequisites

· Python 3.8 or higher (3.9+ recommended for optimal performance)
· macOS, Linux, or Windows (64-bit systems recommended)
· Microphone and speakers/headphones
· At least 4GB RAM (8GB recommended for optimal performance)
· 2GB+ free disk space for model storage

Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Keef98/TransLive
   cd TransLive
   ```
2. Create and activate virtual environment
   ```bash
   # Create virtual environment
   python -m venv translive_env
   
   # Activate on macOS/Linux
   source translive_env/bin/activate
   
   # Activate on Windows
   translive_env\Scripts\activate
   ```
3. Install system dependencies
   ```bash
   # On Ubuntu/Debian
   sudo apt-get install portaudio19-dev ffmpeg
   
   # On macOS with Homebrew
   brew install portaudio ffmpeg
   
   # On Windows (ensure Chocolatey is installed)
   choco install portaudio ffmpeg
   ```
4. Install Python dependencies
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Download and configure models
   ```bash
   # Download Whisper model (base recommended for balance of speed/accuracy)
   python -c "import whisper; whisper.load_model('base')"
   
   # Download Argos Translate packages
   python -c "import argostranslate; argostranslate.package.update_package_index(); packages = argostranslate.package.get_available_packages(); package_to_install = next(filter(lambda x: x.from_code == 'en' and x.to_code == 'fr', packages)); argostranslate.package.install_from_path(package_to_install.download())"
   
   # Download NLTK data
   python -c "import nltk; nltk.download('words', quiet=True)"
   ```
6. Configure audio devices
   ```bash
   # List available audio devices
   python list_devices.py
   
   # Update configuration (see Configuration section below)
   cp config/default_config.yaml config/custom_config.yaml
   # Edit config/custom_config.yaml with your preferred devices
   ```
7. Run the application
   ```bash
   python app.py --config config/custom_config.yaml
   ```

⚙️ Configuration

TransLive supports multiple configuration methods:

YAML Configuration File

Create a config.yaml file with the following structure:

```yaml
audio:
  input_device: 0
  output_device: 1
  sample_rate: 16000
  channels: 1
  silence_threshold: 0.01
  silence_duration: 1.5
  chunk_size: 1024

processing:
  whisper_model: base
  target_language: fr
  min_audio_length: 1.0
  max_audio_length: 10.0

translation:
  source_lang: en
  target_lang: fr
  enable_profanity_filter: true

tts:
  voice_model: tts_models/en/vctk/vits
  speaker: p225
  speech_speed: 1.0

logging:
  level: INFO
  transcript_file: transcripts/translation_log.txt
  max_file_size: 10485760
  backup_count: 5

performance:
  max_queue_size: 10
  processing_timeout: 30
  enable_monitoring: true
```

Environment Variables

All settings can be configured via environment variables:

```bash
export TRANSLIVE_AUDIO_INPUT_DEVICE=0
export TRANSLIVE_AUDIO_SILENCE_THRESHOLD=0.01
export TRANSLIVE_PROCESSING_WHISPER_MODEL=base
export TRANSLIVE_LOGGING_LEVEL=INFO
```

Command Line Arguments

```bash
python app.py --input-device 0 --output-device 1 --model base --language fr --verbose
```

📋 Dependencies

Core Python Libraries

· whisper (>=1.0.0): OpenAI's speech recognition model
· argostranslate (>=1.5.0): Offline translation engine
· TTS (>=0.17.0): Text-to-speech synthesis
· sounddevice (>=0.4.6): Real-time audio I/O
· scipy (>=1.10.0): Audio processing and analysis
· numpy (>=1.24.0): Numerical computations
· nltk (>=3.8.0): Natural language processing
· pyaudio (>=0.2.13): Audio capture utilities
· PyYAML (>=6.0): Configuration management
· requests (>=2.31.0): HTTP requests for package management

System Dependencies

· PortAudio: Cross-platform audio I/O library
· FFmpeg: Multimedia framework for audio processing
· ALSA (Linux): Advanced Linux Sound Architecture
· Core Audio (macOS): macOS audio framework
· WASAPI (Windows): Windows Audio Session API

Model Requirements

· Whisper Models: ~100MB-2.5GB depending on selected model size
· Argos Translate Packages: ~100MB per language pair
· TTS Models: ~500MB-1GB for voice models

🏗️ Architecture

```
TransLive Architecture
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Audio     │  │  Transcript │  │    Configuration    │  │
│  │  Capture    │  │   Manager   │  │     Manager         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Processing Layer                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Speech     │  │ Translation │  │    Text-to-         │  │
│  │ Recognition │  │   Engine    │  │    Speech           │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    System Layer                             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Audio     │  │   Model     │  │     Utilities       │  │
│  │  Subsystem  │  │  Manager    │  │    (Logging,        │  │
│  │             │  │             │  │     Monitoring)     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

🛠️ Troubleshooting

Common Issues

Audio Device Not Found

```bash
# List available audio devices
python list_devices.py

# Check device permissions
# On macOS: System Preferences > Security & Privacy > Microphone
# On Windows: Settings > Privacy > Microphone
# On Linux: Check pulseaudio/alsa configuration
```

Whisper Model Download Issues

```bash
# Manual model download
python -c "
import whisper
import os
os.makedirs('~/.cache/whisper', exist_ok=True)
model = whisper.load_model('base')
"
```

Out of Memory Errors

· Use smaller Whisper model (tiny, base instead of medium, large)
· Reduce chunk_size in configuration
· Close other memory-intensive applications

High CPU Usage

· Use smaller Whisper model
· Increase silence_duration to process less frequently
· Enable hardware acceleration if available

Translation Quality Issues

```bash
# Check installed translation packages
python -c "
import argostranslate.package
packages = argostranslate.package.get_installed_packages()
for p in packages:
    print(f'{p.from_code} -> {p.to_code}')
"
```

Performance Optimization

1. Model Selection:
   · tiny: Fastest, lowest accuracy (~1GB RAM)
   · base: Balanced speed/accuracy (~1.5GB RAM)
   · small: Better accuracy, slower (~2GB RAM)
   · medium: High accuracy, slow (~3.5GB RAM)
   · large: Best accuracy, very slow (~6GB RAM)
2. Audio Settings:
   · Sample rate: 16000Hz (optimal for Whisper)
   · Chunk size: 1024-4096 (adjust based on system)
   · Silence threshold: 0.01-0.05 (adjust for microphone sensitivity)
3. Hardware Acceleration:
   · Enable CUDA for NVIDIA GPUs: pip install whisper-cpp
   · Use Core ML for Apple Silicon: pip install whisper-macos

Debug Mode

Enable verbose logging for troubleshooting:

```bash
python app.py --verbose --log-level DEBUG
```

Check the log files in logs/ directory for detailed error information.

🔧 Advanced Configuration

Custom Voice Models

To use custom TTS voice models:

```yaml
tts:
  voice_model: "path/to/custom/model"
  speaker: "custom_speaker"
  use_cuda: false  # Set to true if you have compatible NVIDIA GPU
```

Language Customization

To add additional languages:

```bash
# List available translation packages
python -c "
import argostranslate.package
packages = argostranslate.package.get_available_packages()
for p in packages:
    print(f'{p.from_code} -> {p.to_code}: {p.package_version}')
"

# Install additional language package
python -c "
import argostranslate.package
package_to_install = [p for p in argostranslate.package.get_available_packages() 
                     if p.from_code == 'en' and p.to_code == 'es'][0]
argostranslate.package.install_from_path(package_to_install.download())
"
```

Bluetooth Audio Configuration

For Bluetooth microphone support:

```bash
# Ensure Bluetooth device is properly paired
# Set as default input device in system settings
# Update configuration with correct device index
```

📊 Performance Monitoring

TransLive includes built-in performance monitoring:

· Real-time CPU/Memory usage display
· Processing latency metrics
· Audio buffer statistics
· Error rate tracking

Enable monitoring in config:

```yaml
performance:
  enable_monitoring: true
  update_interval: 2.0  # seconds
```

🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support

If you encounter issues:

1. Check the Troubleshooting section
2. Search existing GitHub Issues
3. Create a new issue with detailed information including:
   · OS version
   · Python version
   · Error logs
   · Configuration details

🔄 Version Information

· Current Version: 1.0.0
· Whisper Version: 1.0.0
· Argos Translate Version: 1.5.0
· TTS Version: 0.17.0

---

Note: First-time setup may take several minutes due to model downloads. Subsequent runs will be significantly faster as models are cached locally.
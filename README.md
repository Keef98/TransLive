````markdown
# TransLive 🎤🔁🔊

### The Ultimate Offline Live Translation Tool

TransLive is a powerful, real-time translation application that works completely offline. It captures live audio, transcribes speech, translates the text, and then converts the translation back into natural-sounding speech. Built for privacy and performance, TransLive is perfect for use in any environment without an internet connection.

---

### Key Features

* **Real-time Audio Processing:** Experience seamless translation with intelligent silence detection that processes speech in natural pauses.
* **Offline First:** Once set up, TransLive works entirely offline, ensuring your data remains private and secure.
* **Advanced Speech-to-Text:** Powered by **OpenAI's Whisper AI** for highly accurate, fast transcription.
* **High-Quality Translation:** Uses **Argos Translate** for reliable offline English-to-French translation.
* **Natural-Sounding Speech:** Converts translated text into clear, natural speech using state-of-the-art **Text-to-Speech (TTS)** models.
* **Smart Filtering:** Advanced filters remove noise, repetitions, and non-English words for cleaner transcriptions.
* **Cross-Platform:** Works flawlessly on macOS, Linux, and Windows.
* **Highly Configurable:** Customize everything from audio devices and sensitivity to model selection and performance settings.

---

### Quick Start

#### Prerequisites

* **Python:** Version 3.8 or higher (3.9+ recommended)
* **OS:** macOS, Linux, or Windows (64-bit)
* **Hardware:** Microphone, speakers/headphones, 4GB+ RAM (8GB recommended), and 2GB+ free disk space.

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Keef98/TransLive](https://github.com/Keef98/TransLive)
    cd TransLive
    ```

2.  **Set up the virtual environment:**
    ```bash
    # Create the environment
    python -m venv translive_env
    
    # Activate on macOS/Linux
    source translive_env/bin/activate
    
    # Activate on Windows
    translive_env\Scripts\activate
    ```

3.  **Install system dependencies:**
    ```bash
    # On Ubuntu/Debian
    sudo apt-get install portaudio19-dev ffmpeg
    
    # On macOS with Homebrew
    brew install portaudio ffmpeg
    
    # On Windows with Chocolatey
    choco install portaudio ffmpeg
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

5.  **Download and configure models:**
    ```bash
    # Download the Whisper model (we recommend `base` for a good balance of speed and accuracy)
    python -c "import whisper; whisper.load_model('base')"
    
    # Download the Argos Translate English-to-French package
    python -c "import argostranslate; argostranslate.package.update_package_index(); packages = argostranslate.package.get_available_packages(); package_to_install = next(filter(lambda x: x.from_code == 'en' and x.to_code == 'fr', packages)); argostranslate.package.install_from_path(package_to_install.download())"
    
    # Download NLTK data for text filtering
    python -c "import nltk; nltk.download('words', quiet=True)"
    ```

6.  **Configure audio devices:**
    First, list your available devices:
    ```bash
    python list_devices.py
    ```
    Then, create and edit your custom configuration file:
    ```bash
    cp config/default_config.yaml config/custom_config.yaml
    ```
    Open `config/custom_config.yaml` and update the `input_device` and `output_device` IDs with the correct values from the previous step.

7.  **Run the application:**
    ```bash
    python app.py --config config/custom_config.yaml
    ```

> **Note:** The first run may take a few minutes to complete the model downloads. Subsequent runs will be much faster as the models are cached locally.

---

### Configuration

TransLive is highly customizable via three methods.

#### 1. YAML Configuration File

Modify `config/custom_config.yaml` with your preferred settings.

```yaml
audio:
  input_device: 0
  output_device: 1
  sample_rate: 16000
  silence_duration: 1.5

processing:
  whisper_model: base
  target_language: fr

translation:
  source_lang: en
  target_lang: fr

logging:
  transcript_file: transcripts/translation_log.txt

performance:
  enable_monitoring: true
````

#### 2\. Environment Variables

You can override any setting using environment variables prefixed with `TRANSLIVE_`.

```bash
export TRANSLIVE_AUDIO_INPUT_DEVICE=0
export TRANSLIVE_PROCESSING_WHISPER_MODEL=base
```

#### 3\. Command Line Arguments

For quick adjustments, use command line arguments.

```bash
python app.py --input-device 0 --output-device 1 --model base
```

-----

### Architecture

TransLive is built on a modular, multi-threaded architecture designed for robust real-time performance. The system is composed of four main components that work together in a producer-consumer model.

1.  **Audio Capture & Processing:** The application continuously captures audio from the microphone. It uses a sophisticated **silence detection algorithm** to identify segments of speech. This ensures that the system only processes meaningful audio, reducing latency and resource usage. When a pause is detected, the audio segment is passed to the next stage.
2.  **Speech Recognition:** The captured audio segment is fed to the **Whisper AI model**. The model transcribes the speech into English text. This component runs in a dedicated thread to avoid blocking the audio stream.
3.  **Translation:** The transcribed text is then sent to the **Argos Translate engine**. This engine, which operates entirely offline, translates the text from English to French.
4.  **Text-to-Speech (TTS) & Playback:** The translated text is passed to the **TTS engine**. It synthesizes the text into a natural-sounding audio clip, which is then played back through the configured output device.

This multi-threaded pipeline ensures that audio can be captured and processed continuously, even as previous segments are being transcribed, translated, and synthesized. The use of a decoupled architecture with clear data flow between components makes the system scalable, robust, and easy to maintain.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/cb18b76d-0f99-49d6-9a67-2d37cbad52be" />


### Troubleshooting & Optimization

#### Common Issues

  * **Audio Device Not Found:**

      * Ensure your microphone is connected and not in use by another application.
      * Check your operating system's privacy settings to ensure the application has microphone access.

  * **Out of Memory Errors:**

      * Use a smaller Whisper model (`tiny` or `base`).
      * Increase the value of `silence_duration` in your config to reduce how often the application processes audio chunks.
      * Close other memory-intensive applications.

  * **High CPU Usage:**

      * Select a smaller Whisper model.
      * Consider increasing `silence_duration` to give your CPU more time between processing cycles.

#### Performance Optimization

1.  **Model Selection:**

      * `tiny`: Fastest, lowest accuracy (\~1GB RAM)
      * `base`: Recommended for balance (\~1.5GB RAM)
      * `small`: Better accuracy, slower (\~2GB RAM)
      * `medium`: High accuracy, slow (\~3.5GB RAM)
      * `large`: Best accuracy, very slow (\~6GB RAM)

2.  **Hardware Acceleration:**

      * **NVIDIA GPU:** Install `whisper-cpp` and enable CUDA for a significant speed boost.
      * **Apple Silicon:** Use Core ML for a performance boost by installing `whisper-macos`.

3.  **Debug Mode:**

      * For detailed logging, run the application with:
        ```bash
        python app.py --verbose --log-level DEBUG
        ```

-----

### Need Help?

If you encounter an issue, please check the **Troubleshooting** section and search existing GitHub Issues. If you can't find a solution, open a new issue and include:

  * Your operating system and version
  * Your Python version
  * Relevant error logs
  * Your configuration details

-----

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

```
```

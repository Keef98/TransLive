import whisper
import argostranslate.package
import argostranslate.translate
from TTS.api import TTS
import platform
import queue
import time
import threading
import os
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import re
from datetime import datetime
import nltk
import string
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer

nltk.data.path.append("/Users/lambertni/nltk_data")
nltk.download("words")

ENGLISH_WORDS = set(words.words())
TOKENIZER = RegexpTokenizer(r"\b[a-zA-Z]+\b")

# Set Devices
INPUT_DEVICE = 1  # Input Device
OUTPUT_DEVICE = 2  # Output Device
SILENCE_THRESHOLD = 50  # Lower value = more sensitive to silence
PAUSE_TIME = 1.5  # Increased pause detection before processing (in seconds)

# Detect Channels
device_info = sd.query_devices(INPUT_DEVICE, "input")
CHANNELS = min(device_info["max_input_channels"], 1)  # Ensure single channel
print(f"🎤 Using {CHANNELS} channels for {device_info['name']}")

# Queue for audio data
audio_queue = queue.Queue()
TRANSCRIPT_FILE = "translation_transcript.txt"

# Save transcript header
with open(TRANSCRIPT_FILE, "w") as f:
    f.write("🎤 TransLive Transcript\n")
    f.write("=" * 50 + "\n")


def save_transcript(original_text, translated_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRANSCRIPT_FILE, "a") as f:
        f.write(f"[{timestamp}] 🗣️ Input (English): {original_text}\n")
        f.write(f"[{timestamp}] 🔁 Output (French): {translated_text}\n")
        f.write("-" * 50 + "\n")


def remove_repetitions(text):
    words = text.split()
    return " ".join(dict.fromkeys(words))


def filter_non_english(text):
    words_list = TOKENIZER.tokenize(text)
    filtered_words = [
        word for word in words_list if word.lower() in ENGLISH_WORDS or word.istitle()
    ]
    return " ".join(filtered_words)


def detect_silence(audio_chunk):
    volume = np.abs(audio_chunk).mean()
    return volume < SILENCE_THRESHOLD


def audio_callback(indata, frames, time, status):
    if status:
        print(f"🔴 Audio Stream Error: {status}", flush=True)
    audio_queue.put(indata.copy())


def start_audio_stream():
    print("🎙️ Listening for audio...")
    with sd.InputStream(
        device=INPUT_DEVICE,
        samplerate=44100,
        channels=CHANNELS,
        dtype="int16",
        callback=audio_callback,
        blocksize=44100,
    ):
        audio_buffer = []
        silence_time = 0

        while True:
            if not audio_queue.empty():
                chunk = audio_queue.get()
                audio_buffer.append(chunk)

                if detect_silence(chunk):
                    if silence_time == 0:
                        silence_time = time.time()
                    elif time.time() - silence_time > PAUSE_TIME:
                        print("✅ Detected Pause: Processing Speech...")
                        process_audio(audio_buffer)
                        audio_buffer.clear()
                        silence_time = 0
                else:
                    silence_time = 0
            time.sleep(0.1)


def process_audio(audio_data):
    full_audio = np.concatenate(audio_data, axis=0)
    recognize_and_translate(full_audio)


def setup_argos_translate():
    model_path = "en_fr.argosmodel"
    if os.path.exists(model_path):
        argostranslate.package.install_from_path(model_path)
        print("✅ Translation model installed!")
    else:
        print("❌ Error: Translation model missing.")
        exit(1)


def recognize_speech_whisper(audio_file):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file, fp16=False, language="en")
    text = remove_repetitions(result["text"])
    text = filter_non_english(text)
    print(f"🎙️ Recognized Speech: {text}")
    return text


def translate_text_offline(text, from_lang="en", to_lang="fr"):
    if not text.strip():
        return "Error: No recognized speech."
    text = re.sub(r"[^a-zA-Z0-9.,!?\' ]", "", text).strip()
    installed_languages = argostranslate.translate.get_installed_languages()
    from_lang_obj = next(
        (lang for lang in installed_languages if lang.code == from_lang), None
    )
    to_lang_obj = next(
        (lang for lang in installed_languages if lang.code == to_lang), None
    )
    if from_lang_obj is None or to_lang_obj is None:
        return "Translation model not available."
    translated_text = from_lang_obj.get_translation(to_lang_obj).translate(text)
    print(f"🔁 Translated Text: {translated_text}")
    return translated_text


tts = TTS("tts_models/en/vctk/vits").to("cpu")  # Supports male voices


def text_to_speech_offline(text):
    print(f"🔊 Speaking: {text}")
    tts.tts_to_file(text=text, file_path="output.wav", speaker="p229")
    if platform.system() == "Darwin":
        os.system(f"ffplay -nodisp -autoexit output.wav")
    elif platform.system() == "Linux":
        os.system(f"aplay -D plughw:{OUTPUT_DEVICE} output.wav")
    elif platform.system() == "Windows":
        os.system("start output.wav")


def recognize_and_translate(audio_chunk):
    try:
        if audio_chunk.size == 0:
            print("⚠️ No audio detected.")
            return
        write("input_audio.wav", 44100, audio_chunk)
        text = recognize_speech_whisper("input_audio.wav")
        if text.strip():
            translated_text = translate_text_offline(text, "en", "fr")
            save_transcript(text, translated_text)
            threading.Thread(
                target=text_to_speech_offline, args=(translated_text,)
            ).start()
    except Exception as e:
        print(f"❌ Error processing audio: {e}")


def main():
    setup_argos_translate()
    print("🚀 Starting real-time audio processing...")
    mic_thread = threading.Thread(target=start_audio_stream, daemon=True)
    mic_thread.start()
    while True:
        time.sleep(5)


if __name__ == "__main__":
    main()

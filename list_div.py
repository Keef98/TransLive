import pyaudio
import sounddevice as sd

def list_audio_devices():
    print(sd.query_devices())

list_audio_devices()


def list_audio_devices():
    audio = pyaudio.PyAudio()
    for i in range(audio.get_device_count()):
        device_info = audio.get_device_info_by_index(i)
        print(f"Device {i}: {device_info['name']}")
    audio.terminate()

list_audio_devices()
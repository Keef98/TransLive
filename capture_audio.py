import pyaudio

def capture_audio_from_bluetooth(device_index, duration=15, rate=44100, chunk_size=1024):
    """
    Captures audio from a Bluetooth microphone using PyAudio.

    :param device_index: The index of the Bluetooth microphone device.
    :param duration: Duration in seconds to capture audio.
    :param rate: Sampling rate of the audio.
    :param chunk_size: Number of frames per buffer.
    :return: Captured audio data.
    """
    audio = pyaudio.PyAudio()

    # Open the stream
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=rate,
                        input=True,
                        input_device_index=device_index,
                        frames_per_buffer=chunk_size)

    print("Recording...")
    frames = []

    # Capture audio for the specified duration
    for _ in range(0, int(rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    return b''.join(frames)

# Example usage
device_index = 0 # Replace with the index of your Bluetooth microphone
audio_data = capture_audio_from_bluetooth(device_index)
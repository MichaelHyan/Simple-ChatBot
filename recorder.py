import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write


def record_audio(duration=5, filename='audio.wav', sample_rate=16000):
    try:
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='float32'
        )
        sd.wait()
        write(filename, sample_rate, (audio * 32767).astype(np.int16))
        print(f"录音完成")
    except Exception as e:
        print(f"录音出错: {e}")

def main():
    sample_rate = 16000
    duration = 5
    filename = f"audio.wav"
    record_audio(duration, filename, sample_rate)

if __name__ == "__main__":
    main()
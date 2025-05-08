import librosa
import numpy as np
def get_wave():
    try:
        audio_data, sample_rate = librosa.load('output.mp3', sr=None)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return []
    samples_per_10ms = int(sample_rate * 0.01)
    out = []
    for i in range(1, len(audio_data), samples_per_10ms):
        loudness = abs(audio_data[i])
        loudness = audio_data[i]
        out.append(loudness * 10)
    return out

def get_wave_max():
    try:
        audio_data, sample_rate = librosa.load('output.mp3', sr=None)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return []
    
    samples_per_10ms = int(sample_rate * 0.01)
    out = []
    
    for i in range(0, len(audio_data) - samples_per_10ms + 1, samples_per_10ms):
        segment = audio_data[i:i + samples_per_10ms]
        max_loudness = np.max(np.abs(segment))
        out.append(max_loudness * 10)
    return out
if __name__ == "__main__":
    a = get_wave_max()
    print(a)
    print(len(a))


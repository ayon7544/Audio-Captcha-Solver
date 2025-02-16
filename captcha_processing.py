import librosa
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

def load_audio(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate

def noise_reduction(audio):
    audio_filtered = librosa.effects.preemphasis(audio)
    return audio_filtered

def normalize_audio(audio):
    max_value = np.max(np.abs(audio))
    if max_value > 0:
        audio_normalized = audio / max_value
    else:
        audio_normalized = audio
    return audio_normalized

def segment_audio_by_silence(audio, sample_rate, top_db=20):
    intervals = librosa.effects.split(audio, top_db=top_db)
    segments = [audio[start:end] for start, end in intervals]
    return segments

def save_audio(audio, sample_rate, filename='cleaned_audio.wav'):
    wav.write(filename, sample_rate, np.int16(audio / np.max(np.abs(audio)) * 32767))

def recognize_audio(filename, language='en-US'):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        print(f"Decoded text: {text}")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Error with the Google Speech Recognition service")

audio, sample_rate = load_audio('captchas/audio/captcha_0001.wav')

audio_clean = noise_reduction(audio)

audio_normalized = normalize_audio(audio_clean)

save_audio(audio_normalized, sample_rate, 'cleaned_normalized_audio.wav')

print("Recognizing text from entire cleaned audio...")
recognize_audio('captchas/audio/captcha_0001.wav')

audio_segments = segment_audio_by_silence(audio, sample_rate, top_db=20)

for idx, segment in enumerate(audio_segments):
    segment_filename = f'segment_{idx + 1}.wav'
    save_audio(segment, sample_rate, segment_filename)
    print(f"Recognizing text from segment {idx + 1}...")
    recognize_audio(segment_filename)

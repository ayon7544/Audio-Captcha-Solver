# Audio-Captcha-Solver
Here's a README for the provided code:

---

# Audio Processing and Speech Recognition

This project implements a set of tools for audio processing, noise reduction, and speech recognition using Python. It includes functions to load, clean, normalize, segment audio files, and use speech recognition to extract text from audio files. The goal is to process and transcribe audio files effectively.

## Overview

The solution involves multiple steps:
1. **Loading audio** from a file.
2. **Noise reduction** to enhance audio clarity using a preemphasis filter.
3. **Normalization** to scale the audio into a manageable range.
4. **Segmentation** of audio based on silence, which helps identify distinct parts of speech.
5. **Speech recognition** to transcribe the audio content into text.

## Setup Instructions

Follow the steps below to set up and run this solution:

### 1. Clone the repository


git clone https://github.com/ayon7544/Audio-Captcha-Solver.git
cd Audio-Captcha-Solver


download dataset into the folder 

### 2. Install dependencies

This solution requires several Python libraries: `librosa`, `numpy`, `scipy`, and `speech_recognition`. You can install the required libraries via `pip` by running:

pip install -r requirements.txt


If you do not have a `requirements.txt` file, you can manually install the dependencies:

pip install librosa numpy scipy SpeechRecognition

### 3. Prepare your audio file

The audio file should be in `.wav` format. The code assumes the presence of an audio file to process. Update the file path in the script (e.g., `'captchas/audio/captcha_0001.wav'`) to point to your audio file.

### 4. Run the solution

Once you've set up the environment and prepared your audio, you can run the solution with:

python captcha_processing.py


This will perform the following tasks:
- Load the audio file.
- Apply noise reduction and normalization.
- Save the cleaned audio as a new `.wav` file.
- Perform speech recognition on the entire audio file.
- Segment the audio based on silence, process each segment, and perform speech recognition on each segment individually.

---

## High-Level Approach

The code processes audio in several stages:

1. **Loading the Audio**:
   - The audio file is loaded using the `librosa` library, which reads the audio into a waveform and extracts the sample rate.
   
2. **Noise Reduction**:
   - A preemphasis filter is applied to the audio using `librosa.effects.preemphasis`. This filter emphasizes high frequencies and reduces low-frequency noise, which is common in speech.

3. **Normalization**:
   - The audio is normalized to a range of [-1, 1] by dividing each audio sample by the maximum absolute value of the waveform. This step ensures that the audio has a consistent volume level.

4. **Segmentation**:
   - The audio is split into segments based on silence detection. The silence detection algorithm in `librosa.effects.split()` identifies portions of the audio with low energy, effectively segmenting it into meaningful parts like words or phrases.

5. **Speech Recognition**:
   - The audio is passed through the Google Speech Recognition API using the `speech_recognition` library. The text is extracted from both the entire cleaned audio and each of the individual segments.

---

## Design Decisions

- **Library Choice**:
  - `librosa` was chosen for its extensive functionality in handling audio data and its ability to perform various transformations like noise reduction and segmentation.
  - `speech_recognition` was chosen for its simple integration with the Google Speech Recognition API to convert speech into text.
  
- **Noise Reduction**:
  - A simple preemphasis filter was chosen to remove low frequencies and enhance higher frequencies where speech typically occurs. This method is quick and effective but may not handle more complex noise scenarios.
  
- **Audio Segmentation**:
  - The audio is segmented based on silence detection using `librosa.effects.split()`. This approach is efficient for detecting pauses in speech, such as the separation between words or phrases.

- **Speech Recognition**:
  - The speech recognition uses the Google Speech Recognition API, which is easy to integrate and performs well in real-time applications. The code attempts to recognize the entire audio as well as individual segments.

---

## Assumptions

- The input audio is in `.wav` format.
- The audio file is of relatively good quality. If there is significant background noise or distortion, additional noise reduction techniques might be needed.
- Google Speech Recognition API works without issues (requires an internet connection).

---

## Example Output

After running the script, the following files will be generated:
- `cleaned_normalized_audio.wav`: The cleaned and normalized version of the original audio.
- `segment_X.wav`: Individual segments of the audio, where `X` is the segment number.
- Each segment and the entire audio file will be transcribed, and the transcriptions will be printed in the console.

---

## Troubleshooting

- **Could not understand audio**: This error typically occurs if the audio is too noisy or unclear. Consider applying additional noise reduction techniques or using a higher-quality audio file.
- **Error with the Google Speech Recognition service**: This might happen due to a network issue or if the Google API is down. Try again later or check your network connection.

---

Feel free to modify or extend the code to fit your specific use case. Happy coding!
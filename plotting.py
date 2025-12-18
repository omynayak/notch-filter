from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

samplingRate, data = wavfile.read("audio.wav")

original_dtype = data.dtype

if len(data.shape) > 1:
    data = data.mean(axis=1)

fft_data = np.fft.fft(data)

N = len(data)
frequencies = np.fft.fftfreq(N, 1/samplingRate)
magnitude = np.abs(fft_data)

positive_frequencies = frequencies[:N//2]
positive_magnitude = magnitude[:N//2]


samplingRate1, data1 = wavfile.read("cleaned_audio.wav")

original_dtype1 = data1.dtype
if(len(data1.shape) > 1):
    data1 = data1.mean(axis = 1)

fft1 = np.fft.fft(data1)

N1 = len(data)
frequencies1 = np.fft.fftfreq(N1, 1/samplingRate1)
magnitude1 = np.abs(fft1)

positive_frequencies1 = frequencies1[:N1//2]
positive_magnitude1 = magnitude1[:N1//2]

plt.figure(figsize=(12, 6))
plt.plot(positive_frequencies, positive_magnitude)
plt.title("Frequency Spectrum of the Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(positive_frequencies1, positive_magnitude1)
plt.title("Frequency Spectrum of the Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
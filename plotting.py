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

plt.figure(figsize=(12, 6))
plt.plot(positive_frequencies, positive_magnitude)
plt.title("Frequency Spectrum of the Audio Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
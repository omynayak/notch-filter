from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

# Sample the audio signal: 
samplingRate, data = wavfile.read("audio.wav")
# Keep a copy of the original file encoding for later reconstruction
original_dtype = data.dtype

# make the audio mono for sterio audio
if len(data.shape) > 1:
    data = data.mean(axis=1)

# Apply the fast fourier transform
fft_data = np.fft.fft(data)


N = len(data)
frequencies = np.fft.fftfreq(N, 1/samplingRate)
magnitude = np.abs(fft_data)

fundamental_frequency = 55
for n in range(1,10):
    temp_freq = fundamental_frequency
    temp_freq *= n
    lower_freq = temp_freq - 10
    upper_freq = temp_freq + 10
    indices_to_remove = np.where((np.abs(frequencies) >= lower_freq) & (np.abs(frequencies) <= upper_freq))[0]
    fft_data[indices_to_remove] = 0



# Plotting the new graph: 

N = len(data)
frequencies = np.fft.fftfreq(N, 1/samplingRate)
magnitude = np.abs(fft_data)
positive_frequencies = frequencies[:N//2]
positive_magnitude = magnitude[:N//2]



reconstructed_audio = np.fft.ifft(fft_data)
reconstructed_audio = np.real(reconstructed_audio)

max_original_val = np.iinfo(original_dtype).max
reconstructed_audio = np.interp(reconstructed_audio, (reconstructed_audio.min(), reconstructed_audio.max()), (-max_original_val, max_original_val))
reconstructed_audio = reconstructed_audio.astype(original_dtype)

wavfile.write("cleaned_audio.wav", samplingRate, reconstructed_audio)


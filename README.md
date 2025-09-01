# Basic Notch Filter

## What is it
- A basic notch filter written in Python that:
    1. Samples an input signal, preferably plagued by a signal noise.
    2. Applies the Fast Fourier Transform algorithm on the sampled signal array.
    3. Identifies the fundamental frequency of the noise.
    4. Eliminates the fundamental frequency and the first 5 harmonics
    5. Reconstructs the signal.

## How does it work?
- It works by first sampling the signal, here I have used a Scipy module since the signal is a .wav file.
- Then it deconstructs the signal into its composite frequencies using the FFT algorithm.
- Then it finds the peak of the signal and eliminates the corresponding harmonics.

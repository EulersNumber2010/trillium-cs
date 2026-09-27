import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

def plot_harmonics(harmonics):
    # 1. Create your plot
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("My Plot")

    # 2. Save the figure (Always do this BEFORE calling plt.show())
    plt.savefig('my_plot.png')

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a single sine wave array."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

def additive_synthesis(fundamental_freq, duration, amplitudes, sample_rate=44100):
    """
    Blends multiple harmonic frequencies together.
    
    amplitudes: List of floats representing the volume of each harmonic.
                Index 0 = Fundamental (1x)
                Index 1 = Second harmonic (2x)
                Index 2 = Third harmonic (3x), etc.
    """
    # Initialize an array of zeros with the correct length
    total_samples = int(sample_rate * duration)
    mixed_signal = np.zeros(total_samples)
    
    # Generate and sum each harmonic layer
    for i, amp in enumerate(amplitudes):
        harmonic_num = i + 1  # 1st harmonic, 2nd harmonic, etc.
        freq = fundamental_freq * harmonic_num
        
        # Avoid generating frequencies above the Nyquist frequency (half the sample rate)
        if freq >= sample_rate / 2:
            break
            
        wave = generate_sine_wave(freq, duration, sample_rate)
        mixed_signal += wave * amp
        
    # Prevent digital clipping by normalizing the audio between -1.0 and 1.0
    max_val = np.max(np.abs(mixed_signal))
    if max_val > 0:
        mixed_signal = mixed_signal / max_val
        
    return mixed_signal

# --- Example Usage ---
SAMPLE_RATE = 44100
FUNDAMENTAL = 261.63  # A3 note
DURATION = 2.0       # 2 seconds

# Timbre Recipe (Organ/Square-wave-like character using odd harmonics)
# Fundamental (1.0), 2nd (0.0), 3rd (0.5), 4th (0.0), 5th (0.25)
harmonic_weights = [1.0, 0.0, 0.25, 0.0, 0.0625]

# Generate the synthesized sound
synthesized_audio = additive_synthesis(FUNDAMENTAL, DURATION, harmonic_weights, SAMPLE_RATE)

# Convert to 16-bit PCM WAV format
audio_int16 = (synthesized_audio * 32767).astype(np.int16)
wav.write("additive_synth_output.wav", SAMPLE_RATE, audio_int16)

print("Audio file saved successfully as 'additive_synth_output.wav'")

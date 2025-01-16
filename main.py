
from py_term_helpers import top_wrap, center_string_stars
from ipdb import set_trace
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

amp = 1
freq = 440
dur = 1
samp = 44100

t = np.linspace(0, dur, int(samp * dur), endpoint=False)
sine_wave = amp * np.sin(2 * np.pi * freq * t)

sr_1, wav_1 = wavfile.read('./assets/Squeakies.wav')
sr_2, wav_2 = wavfile.read('./assets/156.wav')
# mp3_1 = wavfile.read('./assets/Multiverse.mp3')

# for x in wav_1[1]:
#     print(x)


def get_min_max(wav):
    # min, max
    mini, maxi = 0, 0
    for x, y in wav:
        mini = min(mini, x, y)
        maxi = max(maxi, x, y)

    return (mini, maxi)


def plot_waveform(t, waveform):
    plt.plot(t, waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()


top_wrap('TESTING')

set_trace()

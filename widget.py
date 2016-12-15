import matplotlib.pyplot as plt
import scipy.io.wavfile as wf
import numpy as np
import wave


class AudioWidget(object):
    def __init__(self, filename):
        # Extract Raw Audio from Wav File
        source = wf.read(filename)
        signal = source[1]
        fs = float(source[0])
        print signal
        print fs

        time = np.linspace(0, len(signal) / fs, num=len(signal))
        print time
        print signal
        plt.figure()
        plt.title('Signal Wave...')
        plt.plot(time, signal)
        self.plt = plt


if __name__ == '__main__':
    widget = AudioWidget("wav/Xe.wav")
    widget.plt.show()

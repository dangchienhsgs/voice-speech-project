from audiolazy.lazy_filters import z, Stream
from widget import AudioWidget
import wave
import numpy as np
import matplotlib.pyplot as plt
from audiolazy.lazy_analysis import window
import scipy.io.wavfile as wf
from audiolazy.lazy_lpc import acorr
from audiolazy.lazy_lpc import lpc


def read_audio(path):
    source = wf.read(path)
    num = source[0]
    data = source[1]

    return num, data


def pre_emphasis(signal):
    start = Stream(signal)
    filter_func = 1 / (1 - z ** -1)
    output = filter_func(start, zero=0).take(len(signal))
    return output


def overlap_analysis_window(signal, window_size, overlap_size):
    if overlap_size > window_size:
        raise Exception("Overlap_size can not larger than window_size {0} > {1}".format(overlap_size, window_size))

    start = 0
    stop = len(signal)

    windows = []
    while start < stop:
        end = min(start + window_size, stop)
        windows.append(signal[start:end])
        start = start + window_size - overlap_size
    return np.array(windows)


def hamming_one_window(signal):
    return window.hamming(len(signal)) * signal


def hamming_many_window(signals):
    return np.array([np.array(window.hamming(len(signal))) * signal for signal in signals])


def auto_correlation(signals, p):
    """
    :param signals:
    :param p: level of auto correlation
    :return:
    """
    return np.array([acorr(signal, max_lag=p) for signal in signals])


def save(path, params, frames):
    file = wave.open(path, "w")
    file.setparams(params)
    file.writeframes(frames)
    file.close()


def combine(signals, overlap_size):
    result = np.array([])
    for i in range(0, len(signals)):
        if i > 0:
            result = np.append(result, signals[i][overlap_size:])
        else:
            result = np.append(result, signals[i])

    return result


def analyze():
    print "Start"
    level = 30
    overlap_size = 0
    window_size = 500
    num_samples, channel = read_audio("wav/Xe.wav")
    print len(channel)

    print "Create overlap analysis window"
    a = overlap_analysis_window(channel, window_size, overlap_size)
    print "Finish create overlap analysis window"

    print "Find LPC parameters"
    filter_function = np.array([lpc.kautocor(w, level) for w in a])
    print "Finish find LPC parameters"

    output = []
    for i in range(0, len(a)):
        output.append(filter_function[i](a[i], zero=0).take(len(a[i])))

    output = combine(np.array(output), overlap_size)
    wf.write("wav/Xe_out.wav", num_samples, output)


def visualize(data, rate, name):
    # Extract Raw Audio from Wav File
    time = np.linspace(0, len(data) / rate, num=len(data))
    plt.figure()
    plt.title('Signal Wave...')
    plt.plot(data)
    plt.savefig(name)


if __name__ == "__main__":
    analyze()

    w1 = read_audio("wav/Xe.wav")
    x1 = w1[1]
    r1 = w1[0]

    print r1

    w2 = read_audio("wav/Xe_out.wav")
    x2 = w2[1]
    r2 = w2[0]
    print r2

    for i in range(0, len(x1), 500):
        visualize(x1[i:min(len(x1), i + 500)], r1, "images/voice_{0}".format(i))
        visualize(x2[i:min(len(x2), i + 500)], r2, "images/source_{0}".format(i))

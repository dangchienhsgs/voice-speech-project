from recorder import *
import numpy as np
from PyQt4 import QtGui, QtCore
from mpl_figure import *


class LiveFFTWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.init_ui()

        # init class data
        self.init_data()

        # connect slots
        self.connect_slots()

        # init MPL widget
        self.init_mpl_widget()

    def init_ui(self):
        hbox_gain = QtGui.QHBoxLayout()
        auto_gain = QtGui.QLabel('Auto gain for frequency spectrum')
        auto_gain_checkbox = QtGui.QCheckBox(checked=True)
        hbox_gain.addWidget(auto_gain)
        hbox_gain.addWidget(auto_gain_checkbox)

        # reference to checkbox
        self.auto_gain_checkbox = auto_gain_checkbox

        hbox_fixed_gain = QtGui.QHBoxLayout()
        fixed_gain = QtGui.QLabel('Manual gain level for frequency spectrum')
        fixed_gain_slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        hbox_fixed_gain.addWidget(fixed_gain)
        hbox_fixed_gain.addWidget(fixed_gain_slider)

        self.fixed_gain_slider = fixed_gain_slider

        vbox = QtGui.QVBoxLayout()

        vbox.addLayout(hbox_gain)
        vbox.addLayout(hbox_fixed_gain)

        # mpl figure
        self.main_figure = MplFigure(self)
        vbox.addWidget(self.main_figure.toolbar)
        vbox.addWidget(self.main_figure.canvas)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('LiveFFT')
        self.show()
        # timer for callbacks, taken from:
        # http://ralsina.me/weblog/posts/BB974.html
        timer = QtCore.QTimer()
        timer.timeout.connect(self.handle_new_data)
        timer.start(100)
        # keep reference to timer
        self.timer = timer

    def init_data(self):
        mic = MicrophoneRecorder()
        mic.start()

        # keeps reference to mic
        self.mic = mic

        # computes the parameters that will be used during plotting
        self.freq_vect = np.fft.rfftfreq(mic.chunksize,
                                         1. / mic.rate)
        self.time_vect = np.arange(mic.chunksize, dtype=np.float32) / mic.rate * 1000

    def connect_slots(self):
        pass

    def init_mpl_widget(self):
        """creates initial matplotlib plots in the main window and keeps
        references for further use"""
        # top plot
        self.ax_top = self.main_figure.figure.add_subplot(211)
        self.ax_top.set_ylim(-50000, 50000)
        self.ax_top.set_xlim(0, self.time_vect.max())
        self.ax_top.set_xlabel(u'time (ms)', fontsize=6)

        # bottom plot
        self.ax_bottom = self.main_figure.figure.add_subplot(212)
        self.ax_bottom.set_ylim(0, 1)
        self.ax_bottom.set_xlim(0, self.freq_vect.max())
        self.ax_bottom.set_xlabel(u'frequency (Hz)', fontsize=6)
        # line objects
        self.line_top, = self.ax_top.plot(self.time_vect,
                                          np.ones_like(self.time_vect))

        self.line_bottom, = self.ax_bottom.plot(self.freq_vect,
                                                np.ones_like(self.freq_vect))

    def handle_new_data(self):
        """ handles the asynchroneously collected sound chunks """
        # gets the latest frames
        frames = self.mic.get_frames()

        if len(frames) > 0:
            # keeps only the last frame
            current_frame = frames[-1]
            # plots the time signal
            self.line_top.set_data(self.time_vect, current_frame)
            # computes and plots the fft signal
            fft_frame = np.fft.rfft(current_frame)
            if self.auto_gain_checkbox.checkState() == QtCore.Qt.Checked:
                fft_frame /= np.abs(fft_frame).max()
            else:
                fft_frame *= (1 + self.fixed_gain_slider.value()) / 5000000.
                # print(np.abs(fft_frame).max())
            self.line_bottom.set_data(self.freq_vect, np.abs(fft_frame))

            # refreshes the plots
            self.main_figure.canvas.draw()

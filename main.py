from PyQt4.QtGui import *
import os
from window import *
from main_gui import window as main_window
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import sys
from PyQt4 import QtCore, QtGui
from lpc import *

current_dir = os.path.dirname(__file__)


class Window(QtGui.QMainWindow, main_window.Ui_MainWindow):
    """
    Main program window.
    """

    def __init__(self, app):
        super(Window, self).__init__()
        self.setupUi(self)
        self.app = app
        self.actionOpen.triggered.connect(self.open_file)
        self.lpcButton.clicked.connect(self.analyze_lpc)
        self.saveSourceVoiceButton.clicked.connect(self.save)
        self.compareButton.clicked.connect(self.compare)
        self.hide_lpc_form_layout()

        # input
        self.input = None
        self.output_signal = None
        self.input_signal = None
        self.rate = None
        self.window_size = None
        self.overlap_size = None

    def hide_lpc_form_layout(self):
        for i in range(0, self.lpcFormLayout.count()):
            self.lpcFormLayout.itemAt(i).widget().hide()

    def show_lpc_form_layout(self):
        for i in range(0, self.lpcFormLayout.count()):
            self.lpcFormLayout.itemAt(i).widget().show()

    def open_file(self):
        # read file path
        dialog = QFileDialog()
        path = dialog.getOpenFileName(caption="Open File")
        self.input = str(path)

        # read signal
        source = wf.read(path)
        self.input_signal = source[1]
        fs = float(source[0])

        canvas = plot(self.input_signal, fs)
        self.figureLayout.addWidget(canvas)
        self.show_lpc_form_layout()

    def analyze_lpc(self):
        self.rate, signal = read_audio(self.input)

        self.window_size = int(self.windowSizeEdit.text())
        self.overlap_size = 0
        level = int(self.lpcLevelEdit.text())
        self.output_signal = analyze(signal, level, self.overlap_size, self.window_size)

        canvas = plot(self.output_signal, self.rate)
        self.figureLayout.addWidget(canvas)

    def save(self):
        dialog = QFileDialog()
        path = dialog.getSaveFileName(caption="Save File")
        wf.write(str(path), self.rate, self.output_signal)

    def compare(self):
        print "Compare"
        s = str(self.frameIndexEdit.text())
        args = s.strip().split("-")

        if len(args) == 1:
            index = int(args[0])
            start = index * self.window_size
            stop = (index + 1) * self.window_size

        else:
            index_start = int(args[0])
            index_stop = int(args[1])
            start = index_start * self.window_size
            stop = (index_stop + 1) * self.window_size

        signal1 = self.input_signal[start:stop]
        signal2 = self.output_signal[start:stop]

        print signal1
        print "-------------------"
        print signal2

        w = CompareDialog(signal1, signal2, self.rate)
        w.exec_()
        return


def plot(signal, rate):
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    # create an axis
    ax = figure.add_subplot(111)

    # discards the old graph
    ax.hold(False)

    time = np.linspace(0, float(len(signal)) / rate, num=len(signal))
    ax.plot(time, signal)

    # refresh canvas
    canvas.draw()
    return canvas


class CompareDialog(QtGui.QDialog):
    def __init__(self, signal1, signal2, rate):
        super(CompareDialog, self).__init__()
        self.signal1 = signal1
        self.signal2 = signal2
        self.rate = rate

        self.mainLayout = QtGui.QHBoxLayout()

        # add all main to the main vLayout
        canvas1 = plot(signal1, rate)
        canvas2 = plot(signal2, rate)

        self.mainLayout.addWidget(canvas1)
        self.mainLayout.addWidget(canvas2)
        self.setLayout(self.mainLayout)


def main():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()

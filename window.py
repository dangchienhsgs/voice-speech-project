from widget import *
from mpl_figure import *


class GraphWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        # customize the UI
        self.audio_widget = None

    def load(self, filename):
        self.audio_widget = AudioWidget(filename)
        # vbox = QtGui.QVBoxLayout()
        self.audio_widget.plt.show()
        # vbox.addWidget(FigureCanvas(self.audio_widget.plt.figure(facecolor='white')))
        # self.setLayout(vbox)
        #
        # self.setGeometry(300, 300, 350, 300)
        # self.setWindowTitle('LiveFFT')
        # self.show()
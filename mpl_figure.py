from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from PyQt4 import QtGui


class MplFigure(object):
    def __init__(self, parent):
        self.figure = plt.figure(facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, parent)
        self.zoom_in = QtGui.QPushButton()
        self.zoom_in.setText("Zoom In")
        self.zoom_out = QtGui.QPushButton()
        self.zoom_out.setText("Zoom Out")

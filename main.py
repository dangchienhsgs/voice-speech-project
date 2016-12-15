from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
from window import *
from main_gui import window as main_window
import sys
from PyQt4 import QtCore, QtGui

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

    def open_file(self):
        dialog = QFileDialog()
        path = dialog.getOpenFileName(caption="Open File")
        widget = AudioWidget(str(path))
        self.layout().addWidget(widget.plt)


def main():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()

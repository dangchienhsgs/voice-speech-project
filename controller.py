from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
from widget import *
from window import *
import sys

current_dir = os.path.dirname(__file__)

Ui_FormClass, UiFormBase = \
    uic.loadUiType(os.path.join(current_dir, "controller.ui"))


class Window(Ui_FormClass, UiFormBase):
    """
    Main program window.
    """

    def __init__(self, app):
        super(Window, self).__init__()
        self.setupUi(self)
        self.app = app
        self.graph = None

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setFilter("Audio file (*.wav)")

        if file_dialog.exec_() == QtGui.QDialog.Accepted:
            filename = str(file_dialog.selectedFiles()[0])
            self.graph = GraphWindow()
            self.graph.load(filename)

    def on_actionRecord_triggered(self):
        # TODO
        print "Record"


def main():
    app = QApplication(sys.argv)
    win = Window(app)
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()

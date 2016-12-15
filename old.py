import sys
from gui import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = LiveFFTWidget()
    sys.exit(app.exec_())

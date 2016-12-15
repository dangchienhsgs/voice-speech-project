# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1187, 652)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mainLayout = QtGui.QGridLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.figureLayout = QtGui.QHBoxLayout()
        self.figureLayout.setObjectName(_fromUtf8("figureLayout"))
        self.mainLayout.addLayout(self.figureLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.lpcFormLayout = QtGui.QGridLayout()
        self.lpcFormLayout.setSpacing(2)
        self.lpcFormLayout.setObjectName(_fromUtf8("lpcFormLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.lpcFormLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lpcLevelEdit = QtGui.QLineEdit(self.centralwidget)
        self.lpcLevelEdit.setObjectName(_fromUtf8("lpcLevelEdit"))
        self.lpcFormLayout.addWidget(self.lpcLevelEdit, 1, 1, 1, 1)
        self.lpcButton = QtGui.QPushButton(self.centralwidget)
        self.lpcButton.setObjectName(_fromUtf8("lpcButton"))
        self.lpcFormLayout.addWidget(self.lpcButton, 2, 0, 1, 1)
        self.saveSourceVoiceButton = QtGui.QPushButton(self.centralwidget)
        self.saveSourceVoiceButton.setObjectName(_fromUtf8("saveSourceVoiceButton"))
        self.lpcFormLayout.addWidget(self.saveSourceVoiceButton, 3, 0, 1, 1)
        self.compareButton = QtGui.QPushButton(self.centralwidget)
        self.compareButton.setObjectName(_fromUtf8("compareButton"))
        self.lpcFormLayout.addWidget(self.compareButton, 4, 0, 1, 1)
        self.windowSizeEdit = QtGui.QLineEdit(self.centralwidget)
        self.windowSizeEdit.setObjectName(_fromUtf8("windowSizeEdit"))
        self.lpcFormLayout.addWidget(self.windowSizeEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lpcFormLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.frameIndexEdit = QtGui.QLineEdit(self.centralwidget)
        self.frameIndexEdit.setObjectName(_fromUtf8("frameIndexEdit"))
        self.lpcFormLayout.addWidget(self.frameIndexEdit, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.lpcFormLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.createLPCFilter = QtGui.QAction(MainWindow)
        self.createLPCFilter.setObjectName(_fromUtf8("createLPCFilter"))
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LPC Analyzer", None))
        self.label.setText(_translate("MainWindow", "Window size ", None))
        self.lpcButton.setText(_translate("MainWindow", "Start", None))
        self.saveSourceVoiceButton.setText(_translate("MainWindow", "Save source voice ", None))
        self.compareButton.setText(_translate("MainWindow", "Compare frame", None))
        self.label_2.setText(_translate("MainWindow", "LPC level", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.createLPCFilter.setText(_translate("MainWindow", "Create LPC filter", None))


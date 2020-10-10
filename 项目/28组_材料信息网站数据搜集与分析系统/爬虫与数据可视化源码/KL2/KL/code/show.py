import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from KL.UIFile.firt import Ui_MainWindow

from KL.UIFile.child import *


class mainCode(QMainWindow, Ui_MainWindow):
    BOPPD = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.BOPPD.clicked.connect(self.BOPPDshow)
        self.CPPD.clicked.connect(self.CPPDshow)
        self.BOPETD.clicked.connect(self.BOPETDshow)
        self.PPDFHZ.clicked.connect(self.PPDFHZshow)
        self.PPZSH.clicked.connect(self.PPZSHshow)
        self.PEZSH.clicked.connect(self.PEZSHshow)
        self.ICIS.clicked.connect(self.ICISshow)


    def BOPPDshow(self):
        self.childForm = BOPPForm()
        self.scrollArea.setWidget(self.childForm)

    def CPPDshow(self):
        self.childForm = CPPDForm()
        self.scrollArea.setWidget(self.childForm)

    def BOPETDshow(self):
        self.childForm = BOPETDForm()
        self.scrollArea.setWidget(self.childForm)

    def PPDFHZshow(self):
        self.childForm = PPDFHZForm()
        self.scrollArea.setWidget(self.childForm)

    def PPZSHshow(self):
        self.childForm = PPZSHForm()
        self.scrollArea.setWidget(self.childForm)

    def PEZSHshow(self):
        self.childForm = PEZSHForm()
        self.scrollArea.setWidget(self.childForm)

    def ICISshow(self):
        self.childForm = ICISForm()
        self.scrollArea.setWidget(self.childForm)


if  __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window = mainCode()
    window.show()
    sys.exit(app.exec_())

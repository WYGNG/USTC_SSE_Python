from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget

from KL.UIFile.BOPPUI import Ui_Form as BOPP_UI
from KL.UIFile.CPPDUI import Ui_Form as CPPD_UI
from KL.UIFile.BOPETDUI import Ui_Form as  BOPETD_UI
from KL.UIFile.PPDFHZUI import Ui_Form as PPDFHZ_UI
from KL.UIFile.PPZSHUI import Ui_Form as PPZSH_UI
from KL.UIFile.PEZSHUI import Ui_Form as PEZSH_UI
from KL.UIFile.ICISUI import Ui_Form as ICIS_UI
from KL.code.queryBOPP import *
from KL.code.queryCPP import *
from KL.code.queryPPZSH import *

class BOPPForm(QWidget, BOPP_UI):
    def __init__(self):
        super(BOPPForm, self).__init__()
        self.setupUi(self)

        self.comboBox_4.currentIndexChanged.connect(self.transPic)  # 变动则执行函数

    def transPic(self):
        key = self.comboBox_4.currentIndex()  # 获取键值
        if key == 0:
            image = QtGui.QPixmap(get_data_BOPP("华北地区"))
        if key == 1:
            image = QtGui.QPixmap(get_data_BOPP("华东地区"))
        if key == 2:
            image = QtGui.QPixmap(get_data_BOPP("华南地区"))
        if key == 3:
            image = QtGui.QPixmap(get_data_BOPP("东北地区"))
        if key == 4:
            image = QtGui.QPixmap(get_data_BOPP("西南地区"))

        self.picture2.setPixmap(image)

class CPPDForm(QWidget, CPPD_UI):
    def __init__(self):
        super(CPPDForm, self).__init__()
        self.setupUi(self)

        self.comboBox_5.currentIndexChanged.connect(self.transPic1)  # 变动则执行函数
        self.comboBox_4.currentIndexChanged.connect(self.transPic2)  # 变动则执行函数

    def transPic1(self):
        key = self.comboBox_5.currentIndex()  # 获取键值
        if key == 0:
            image = QtGui.QPixmap(get_data_limit_CPP("CPP复合膜"))
        if key == 1:
            image = QtGui.QPixmap(get_data_limit_CPP("CPP镀铝基材"))
        if key == 2:
            image = QtGui.QPixmap(get_data_limit_CPP("CPP蒸煮膜"))

        self.picture1.setPixmap(image)

    def transPic2(self):
        key = self.comboBox_4.currentIndex()  # 获取键值
        if key == 0:
            image = QtGui.QPixmap(get_data_CPP("CPP复合膜"))
        if key == 1:
            image = QtGui.QPixmap(get_data_CPP("CPP镀铝基材"))
        if key == 2:
            image = QtGui.QPixmap(get_data_CPP("CPP蒸煮膜"))

        self.picture2.setPixmap(image)


class BOPETDForm(QWidget, CPPD_UI):
    def __init__(self):
        super(BOPETDForm, self).__init__()
        self.setupUi(self)

class BOPETDForm(QWidget, BOPETD_UI):
    def __init__(self):
        super(BOPETDForm, self).__init__()
        self.setupUi(self)

class PPDFHZForm(QWidget, PPDFHZ_UI):
    def __init__(self):
        super(PPDFHZForm, self).__init__()
        self.setupUi(self)

class PPZSHForm(QWidget, PPZSH_UI):
    def __init__(self):
        super(PPZSHForm, self).__init__()
        self.setupUi(self)
        self.comboBox_4.currentIndexChanged.connect(self.transPic)  # 变动则执行函数

    def transPic(self):
        key = self.comboBox_4.currentIndex()  # 获取键值
        if key == 0:
            image = QtGui.QPixmap(get_PPZ_data("BOPP膜料"))
        if key == 1:
            image = QtGui.QPixmap(get_PPZ_data("拉丝"))

        self.picture2.setPixmap(image)

class PEZSHForm(QWidget, PEZSH_UI):
    def __init__(self):
        super(PEZSHForm, self).__init__()
        self.setupUi(self)

class ICISForm(QWidget, ICIS_UI):
    def __init__(self):
        super(ICISForm, self).__init__()
        self.setupUi(self)
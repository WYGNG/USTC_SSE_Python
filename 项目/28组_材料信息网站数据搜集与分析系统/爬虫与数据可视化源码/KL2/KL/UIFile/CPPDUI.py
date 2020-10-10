# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPPDUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from KL.code.queryCPP import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 2005)

        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(660, 1310, 121, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.title1_2 = QtWidgets.QLabel(Form)
        self.title1_2.setGeometry(QtCore.QRect(50, 19, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title1_2.setFont(font)
        self.title1_2.setObjectName("title1_2")

        self.title3_2 = QtWidgets.QLabel(Form)
        self.title3_2.setGeometry(QtCore.QRect(50, 1310, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title3_2.setFont(font)
        self.title3_2.setObjectName("title3_2")

        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(650, 620, 121, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")

        self.title2_2 = QtWidgets.QLabel(Form)
        self.title2_2.setGeometry(QtCore.QRect(50, 620, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title2_2.setFont(font)
        self.title2_2.setObjectName("title2_2")

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 50, 861, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(8)

        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 420, 861, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_4.setItemText(0, _translate("Form", "CPP复合膜"))
        self.comboBox_4.setItemText(1, _translate("Form", "CPP镀铝基材"))
        self.comboBox_4.setItemText(2, _translate("Form", "CPP蒸煮膜"))

        self.title1_2.setText(_translate("Form", "国内CPP产品出厂近期收盘价格变化表（元/吨）"))
        self.title3_2.setText(_translate("Form", "国内CPP产品出厂收盘价格变化统计"))
        self.comboBox_5.setItemText(0, _translate("Form", "CPP复合膜"))
        self.comboBox_5.setItemText(1, _translate("Form", "CPP镀铝基材"))
        self.comboBox_5.setItemText(2, _translate("Form", "CPP蒸煮膜"))

        self.title2_2.setText(_translate("Form", "国内CPP产品出厂一周收盘价格变化统计"))
        self.tableWidget_2.setHorizontalHeaderLabels(get_date_CPP())
        self.tableWidget_2.setVerticalHeaderLabels(
            ['CPP复合膜', '', '', 'CPP镀铝基材', '', '', 'CPP蒸煮膜', ''])
        self.tableWidget_2.setItem(0, 0, QTableWidgetItem("华北地区"))
        self.tableWidget_2.setItem(1, 0, QTableWidgetItem("华东地区"))
        self.tableWidget_2.setItem(2, 0, QTableWidgetItem("华南地区"))
        self.tableWidget_2.setItem(3, 0, QTableWidgetItem("华北地区"))
        self.tableWidget_2.setItem(4, 0, QTableWidgetItem("华东地区"))
        self.tableWidget_2.setItem(5, 0, QTableWidgetItem("华南地区"))
        self.tableWidget_2.setItem(6, 0, QTableWidgetItem("华北地区"))
        self.tableWidget_2.setItem(7, 0, QTableWidgetItem("华南地区"))

        items = get_table_CPP()
        for i in range(len(items)):
            item = items[i]
            for j in range(len(item)):
                self.tableWidget_2.setItem(i, j+1, QTableWidgetItem(items[i][j]))

        datetime = get_forecast_CPP().get("datetime")
        forecast = get_forecast_CPP().get("forecast")
        self.textBrowser_2.setText(_translate("Form", "后市分析预测("+datetime+")：\n"+forecast))

        self.picture1 = QtWidgets.QLabel(Form)
        self.picture1.setGeometry(QtCore.QRect(50, 670, 861, 600))
        self.picture1.setScaledContents(True)
        image = QtGui.QPixmap(get_data_limit_CPP("CPP复合膜"))
        self.picture1.setPixmap(image)

        self.picture2 = QtWidgets.QLabel(Form)
        self.picture2.setGeometry(QtCore.QRect(50, 1360, 861, 540))
        self.picture2.setScaledContents(True)
        image2 = QtGui.QPixmap(get_data_CPP("CPP复合膜"))
        self.picture2.setPixmap(image2)
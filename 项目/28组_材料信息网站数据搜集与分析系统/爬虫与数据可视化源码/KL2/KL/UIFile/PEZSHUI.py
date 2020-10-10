# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PEZSHUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from KL.code.queryPEZSH import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(953, 1479)

        self.title1_2 = QtWidgets.QLabel(Form)
        self.title1_2.setGeometry(QtCore.QRect(50, 19, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title1_2.setFont(font)
        self.title1_2.setObjectName("title1_2")

        self.title3_2 = QtWidgets.QLabel(Form)
        self.title3_2.setGeometry(QtCore.QRect(50, 830, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title3_2.setFont(font)
        self.title3_2.setObjectName("title3_2")

        self.title2_2 = QtWidgets.QLabel(Form)
        self.title2_2.setGeometry(QtCore.QRect(50, 220, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title2_2.setFont(font)
        self.title2_2.setObjectName("title2_2")

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 50, 861, 121))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title1_2.setText(_translate("Form", "PE出厂：国内中石化出厂产品近期收盘价格变化表（元/吨）"))
        self.title3_2.setText(_translate("Form", "PE出厂：国内中石化出厂产品收盘价格变化统计"))
        self.title2_2.setText(_translate("Form", "PE出厂：国内中石化出厂产品一周收盘价格变化统计"))

        self.tableWidget_2.setHorizontalHeaderLabels(get_date_PEZSH())
        self.tableWidget_2.setVerticalHeaderLabels(['上海石化膜料', '扬子石化膜料'])

        items = get_table_PEZSH()
        for i in range(len(items)):
            item = items[i]
            for j in range(len(item)):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(items[i][j]))

        self.picture1 = QtWidgets.QLabel(Form)
        self.picture1.setGeometry(QtCore.QRect(50, 258, 861, 541))
        image = QtGui.QPixmap(get_PE_data_week())
        self.picture1.setScaledContents(True)
        self.picture1.setPixmap(image)

        self.picture2 = QtWidgets.QLabel(Form)
        self.picture2.setGeometry(QtCore.QRect(50, 870, 861, 541))
        image2 = QtGui.QPixmap(get_PE_data())
        self.picture2.setScaledContents(True)
        self.picture2.setPixmap(image2)

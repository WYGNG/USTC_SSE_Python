# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ICISUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from KL.code.queryICIS import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 812)

        self.title1_2 = QtWidgets.QLabel(Form)
        self.title1_2.setGeometry(QtCore.QRect(50, 19, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title1_2.setFont(font)
        self.title1_2.setObjectName("title1_2")
        self.title2_2 = QtWidgets.QLabel(Form)
        self.title2_2.setGeometry(QtCore.QRect(50, 210, 668, 25))
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
        self.title1_2.setText(_translate("Form", "BOPP Film:CTR China Import近期价格变化表（美元/吨）"))
        self.title2_2.setText(_translate("Form", "BOPP Film:CTR China Import近期价格变化统计"))

        self.tableWidget_2.setHorizontalHeaderLabels(get_date_ICIS())
        self.tableWidget_2.setVerticalHeaderLabels(['最高价格', '最低价格'])
        items = get_table_ICIS()
        for i in range(len(items)):
            item = items[i]
            for j in range(len(item)):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(items[i][j]))

        self.picture1 = QtWidgets.QLabel(Form)
        self.picture1.setGeometry(QtCore.QRect(50, 250, 861, 541))
        image = QtGui.QPixmap(get_data_ICIS())
        self.picture1.setScaledContents(True)
        self.picture1.setPixmap(image)
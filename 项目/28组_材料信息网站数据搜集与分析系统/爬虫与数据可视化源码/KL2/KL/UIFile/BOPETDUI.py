# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BOPETDUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from KL.code.queryBOPET import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 1651)

        # 设置近三天价格变化表标题
        self.title1 = QtWidgets.QLabel(Form)
        self.title1.setGeometry(QtCore.QRect(50, 19, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title1.setFont(font)
        self.title1.setObjectName("title1")

        # 设置一周内价格变动图片标题
        self.title2 = QtWidgets.QLabel(Form)
        self.title2.setGeometry(QtCore.QRect(50, 290, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title2.setFont(font)
        self.title2.setObjectName("title2")

        # 设置总体价格变动表图片标题
        self.title3 = QtWidgets.QLabel(Form)
        self.title3.setGeometry(QtCore.QRect(70, 900, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title3.setFont(font)
        self.title3.setObjectName("title3")

        # 表格内容
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 861, 81))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)

        # 文本域内容
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(50, 170, 861, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title1.setText(_translate("Form", "国内BOPET产品出厂近期收盘价格变化表（元/吨）"))
        self.title2.setText(_translate("Form", "国内BOPET产品出厂一周收盘价格统计"))
        self.title3.setText(_translate("Form", "国内BOPET产品出厂收盘价格统计"))

        self.tableWidget.setHorizontalHeaderLabels(get_date_BOPET())
        self.tableWidget.setVerticalHeaderLabels(['绍兴翔宇：12μ印刷膜/镀铝基材'])

        items = get_table_BOPET()
        for i in range(len(items)):
            item = items[i]
            for j in range(len(item)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(items[i][j]))

        datetime = get_forecast_BOPP().get("date")
        forecast = get_forecast_BOPP().get("BOPET_futures_analysis")
        self.textBrowser.setText(_translate("Form", datetime+"期货市场:\n"+forecast))

        self.picture1 = QtWidgets.QLabel(Form)
        self.picture1.setGeometry(QtCore.QRect(50, 330, 861, 541))
        image = QtGui.QPixmap(get_data_limit_BOPET())
        self.picture1.setScaledContents(True)
        self.picture1.setPixmap(image)

        self.picture2 = QtWidgets.QLabel(Form)
        self.picture2.setGeometry(QtCore.QRect(50, 950, 861, 540))
        image2 = QtGui.QPixmap(get_data_BOPET(1))
        self.picture2.setScaledContents(True)
        self.picture2.setPixmap(image2)
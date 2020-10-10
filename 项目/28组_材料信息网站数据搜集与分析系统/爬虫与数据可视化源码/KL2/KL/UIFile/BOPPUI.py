# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BOPPUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from KL.code.queryBOPP import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 1832)

        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(660, 1100, 101, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
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
        self.title3_2.setGeometry(QtCore.QRect(50, 1100, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title3_2.setFont(font)
        self.title3_2.setObjectName("title3_2")

        self.title2_2 = QtWidgets.QLabel(Form)
        self.title2_2.setGeometry(QtCore.QRect(50, 450, 668, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.title2_2.setFont(font)
        self.title2_2.setObjectName("title2_2")

        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 50, 861, 231))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(5)

        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 300, 861, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_4.setItemText(0, _translate("Form", "华北地区"))
        self.comboBox_4.setItemText(1, _translate("Form", "华东地区"))
        self.comboBox_4.setItemText(2, _translate("Form", "华南地区"))
        self.comboBox_4.setItemText(3, _translate("Form", "东北地区"))
        self.comboBox_4.setItemText(4, _translate("Form", "西南地区"))

        self.title1_2.setText(_translate("Form", "国内BOPP复合膜出厂近期收盘价格变化表（元/吨）"))
        self.title3_2.setText(_translate("Form", "国内BOPP复合膜出厂收盘价格变化统计（按地区）"))


        self.title2_2.setText(_translate("Form", "国内BOPP复合膜出厂一周收盘价格变化统计"))
        self.tableWidget_2.setHorizontalHeaderLabels(get_date_BOPP())
        self.tableWidget_2.setVerticalHeaderLabels(['华北地区', '华东地区', '华南地区', '东北地区', '西南地区'])
        # 查询数据库，查询近期五天的价格信息
        items = get_table_BOPP()
        # 将价格信息遍历写入表格中
        for i in range(len(items)):
            item = items[i]
            for j in range(len(item)):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(items[i][j]))

        # 查询数据库，查询数据库最新一条的记录，获取最新日评的更新时间和价格走势分析预测
        datetime = get_forecast_BOPP().get("datetime")
        forecast = get_forecast_BOPP().get("forecast")
        self.textBrowser_2.setText(_translate("Form", "BOPP走势分析预测("+datetime+")：\n"+forecast))

        # 设置图形界面中近期一周价格走势的折线图，调用Matplotlib绘图方法，数据来自数据库
        self.picture1 = QtWidgets.QLabel(Form)
        self.picture1.setGeometry(QtCore.QRect(50, 500, 861, 540))
        self.picture1.setScaledContents(True)
        image = QtGui.QPixmap(get_data_limit_BOPP())
        self.picture1.setPixmap(image)
        # 设置图形界面中长期价格走势的折线图，调用Matplotlib绘图方法，数据来自数据库
        self.picture2 = QtWidgets.QLabel(Form)
        self.picture2.setGeometry(QtCore.QRect(50, 1150, 861, 540))
        self.picture2.setScaledContents(True)
        image2 = QtGui.QPixmap(get_data_BOPP("华北地区"))
        self.picture2.setPixmap(image2)
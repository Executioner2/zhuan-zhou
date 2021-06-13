# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 641, 461))
        self.mainWidget.setObjectName("mainWidget")
        self.rightWidget = QtWidgets.QWidget(self.mainWidget)
        self.rightWidget.setGeometry(QtCore.QRect(150, 0, 491, 461))
        self.rightWidget.setObjectName("rightWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.rightWidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 489, 331))
        self.scrollArea.setStyleSheet("#scrollWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setGeometry(QtCore.QRect(0, -42, 468, 371))
        self.scrollWidget.setMinimumSize(QtCore.QSize(400, 371))
        self.scrollWidget.setObjectName("scrollWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 30, 151, 61))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"border: 2px solid gainsboro;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.label_2.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border-radius: 20px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.sendDateTimeLab = QtWidgets.QLabel(self.widget)
        self.sendDateTimeLab.setGeometry(QtCore.QRect(10, 10, 167, 15))
        self.sendDateTimeLab.setStyleSheet("")
        self.sendDateTimeLab.setObjectName("sendDateTimeLab")
        self.verticalLayout.addWidget(self.widget)
        self.sendWidget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.sendWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sendWidget.setStyleSheet("text-align: right;\n"
"")
        self.sendWidget.setObjectName("sendWidget")
        self.label_3 = QtWidgets.QLabel(self.sendWidget)
        self.label_3.setGeometry(QtCore.QRect(320, 40, 81, 41))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"border: 2px solid gainsboro;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.sendWidget)
        self.label_4.setGeometry(QtCore.QRect(420, 40, 41, 41))
        self.label_4.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"border-radius: 20px")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.sendDateTimeLab_2 = QtWidgets.QLabel(self.sendWidget)
        self.sendDateTimeLab_2.setGeometry(QtCore.QRect(270, 10, 191, 16))
        self.sendDateTimeLab_2.setStyleSheet("")
        self.sendDateTimeLab_2.setObjectName("sendDateTimeLab_2")
        self.verticalLayout.addWidget(self.sendWidget)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(70, 40, 61, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"border: 2px solid gainsboro;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius: 20px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.sendDateTimeLab_3 = QtWidgets.QLabel(self.widget_2)
        self.sendDateTimeLab_3.setGeometry(QtCore.QRect(10, 10, 187, 15))
        self.sendDateTimeLab_3.setStyleSheet("")
        self.sendDateTimeLab_3.setObjectName("sendDateTimeLab_3")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(70, 40, 61, 41))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 10px;\n"
"border: 2px solid gainsboro;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 41, 41))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-radius: 20px")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.sendDateTimeLab_4 = QtWidgets.QLabel(self.widget_3)
        self.sendDateTimeLab_4.setGeometry(QtCore.QRect(10, 10, 187, 15))
        self.sendDateTimeLab_4.setObjectName("sendDateTimeLab_4")
        self.verticalLayout.addWidget(self.widget_3)
        self.scrollArea.setWidget(self.scrollWidget)
        self.msgWidget = QtWidgets.QWidget(self.rightWidget)
        self.msgWidget.setGeometry(QtCore.QRect(0, 340, 491, 121))
        self.msgWidget.setObjectName("msgWidget")
        self.textEdit = QtWidgets.QTextEdit(self.msgWidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 489, 121))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setStyleSheet("padding: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushBtn = QtWidgets.QPushButton(self.msgWidget)
        self.pushBtn.setGeometry(QtCore.QRect(390, 80, 91, 28))
        self.pushBtn.setObjectName("pushBtn")
        self.leftWidget = QtWidgets.QWidget(self.mainWidget)
        self.leftWidget.setGeometry(QtCore.QRect(0, 0, 141, 461))
        self.leftWidget.setObjectName("leftWidget")
        self.groupList = QtWidgets.QListWidget(self.leftWidget)
        self.groupList.setGeometry(QtCore.QRect(0, 0, 141, 461))
        self.groupList.setObjectName("groupList")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "你好我好大家好！\n"
"哈哈"))
        self.sendDateTimeLab.setText(_translate("MainWindow", "10032 2021/6/3 19:51"))
        self.label_3.setText(_translate("MainWindow", "大聪明！"))
        self.sendDateTimeLab_2.setText(_translate("MainWindow", "2021/6/3 19:52 2Exectuioner "))
        self.label_5.setText(_translate("MainWindow", "傻逼！"))
        self.sendDateTimeLab_3.setText(_translate("MainWindow", "道德天尊 2021/6/3 19:54"))
        self.label_7.setText(_translate("MainWindow", "傻逼！"))
        self.sendDateTimeLab_4.setText(_translate("MainWindow", "道德天尊  2021/6/3 19:54"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.16364pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">此处输入文字...</span></p></body></html>"))
        self.pushBtn.setText(_translate("MainWindow", "发送"))
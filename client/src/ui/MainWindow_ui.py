# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from client.src.handler import MyTextEdit, MyLabel, MyWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 454)
        MainWindow.setMinimumSize(QtCore.QSize(667, 454))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 87 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.groupVL = QtWidgets.QVBoxLayout()
        self.groupVL.setObjectName("groupVL")
        self.group1 = MyWidget.MyWidget(self.widget)
        self.group1.setMinimumSize(QtCore.QSize(0, 51))
        self.group1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.group1.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.group1.setObjectName("group1")
        self.layoutWidget_4 = QtWidgets.QWidget(self.group1)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 0, 185, 53))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(5, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.groupHead_1 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupHead_1.sizePolicy().hasHeightForWidth())
        self.groupHead_1.setSizePolicy(sizePolicy)
        self.groupHead_1.setMinimumSize(QtCore.QSize(51, 51))
        self.groupHead_1.setMaximumSize(QtCore.QSize(51, 51))
        self.groupHead_1.setStyleSheet("")
        self.groupHead_1.setText("")
        self.groupHead_1.setPixmap(QtGui.QPixmap(":/image/group_1"))
        self.groupHead_1.setScaledContents(True)
        self.groupHead_1.setObjectName("groupHead_1")
        self.horizontalLayout_6.addWidget(self.groupHead_1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 51))
        self.label_13.setMaximumSize(QtCore.QSize(115, 51))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.groupVL.addWidget(self.group1)
        self.group2 = MyWidget.MyWidget(self.widget)
        self.group2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group2.sizePolicy().hasHeightForWidth())
        self.group2.setSizePolicy(sizePolicy)
        self.group2.setMinimumSize(QtCore.QSize(115, 51))
        self.group2.setMaximumSize(QtCore.QSize(200, 51))
        self.group2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.group2.setObjectName("group2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.group2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 185, 53))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(5, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.groupHead_2 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupHead_2.sizePolicy().hasHeightForWidth())
        self.groupHead_2.setSizePolicy(sizePolicy)
        self.groupHead_2.setMinimumSize(QtCore.QSize(51, 51))
        self.groupHead_2.setMaximumSize(QtCore.QSize(51, 51))
        self.groupHead_2.setStyleSheet("")
        self.groupHead_2.setText("")
        self.groupHead_2.setPixmap(QtGui.QPixmap(":/image/group_2"))
        self.groupHead_2.setScaledContents(True)
        self.groupHead_2.setObjectName("groupHead_2")
        self.horizontalLayout_4.addWidget(self.groupHead_2)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(115, 51))
        self.label_9.setMaximumSize(QtCore.QSize(115, 51))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.groupVL.addWidget(self.group2)
        self.group3 = MyWidget.MyWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group3.sizePolicy().hasHeightForWidth())
        self.group3.setSizePolicy(sizePolicy)
        self.group3.setMinimumSize(QtCore.QSize(185, 51))
        self.group3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.group3.setObjectName("group3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.group3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 185, 53))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(5, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.groupHead_3 = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupHead_3.sizePolicy().hasHeightForWidth())
        self.groupHead_3.setSizePolicy(sizePolicy)
        self.groupHead_3.setMinimumSize(QtCore.QSize(51, 51))
        self.groupHead_3.setMaximumSize(QtCore.QSize(51, 51))
        self.groupHead_3.setStyleSheet("")
        self.groupHead_3.setText("")
        self.groupHead_3.setPixmap(QtGui.QPixmap(":/image/group_3"))
        self.groupHead_3.setScaledContents(True)
        self.groupHead_3.setObjectName("groupHead_3")
        self.horizontalLayout_5.addWidget(self.groupHead_3)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(115, 51))
        self.label_11.setMaximumSize(QtCore.QSize(115, 51))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.groupVL.addWidget(self.group3)
        self.verticalLayout_4.addLayout(self.groupVL)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.chatLayout = QtWidgets.QVBoxLayout()
        self.chatLayout.setObjectName("chatLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("#scrollWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setGeometry(QtCore.QRect(0, 0, 428, 291))
        self.scrollWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollWidget.setObjectName("scrollWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msgHistoryLabel = MyLabel.MyLabel(self.verticalLayoutWidget)
        self.msgHistoryLabel.setEnabled(True)
        self.msgHistoryLabel.setMaximumSize(QtCore.QSize(16777215, 16))
        self.msgHistoryLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.msgHistoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgHistoryLabel.setObjectName("msgHistoryLabel")
        self.verticalLayout.addWidget(self.msgHistoryLabel)
        self.scrollArea.setWidget(self.scrollWidget)
        self.chatLayout.addWidget(self.scrollArea)
        self.textEdit = MyTextEdit.MyTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setStyleSheet("padding: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.chatLayout.addWidget(self.textEdit)
        self.pushBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pushBtn.setObjectName("pushBtn")
        self.chatLayout.addWidget(self.pushBtn, 0, QtCore.Qt.AlignRight)
        self.chatLayout.setStretch(0, 4)
        self.chatLayout.setStretch(1, 1)
        self.chatLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.chatLayout, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "群组"))
        self.label_13.setText(_translate("MainWindow", "<$ÿĀ>(〃°ω°〃)<$ÿĀ>"))
        self.label_9.setText(_translate("MainWindow", "六世同堂"))
        self.label_11.setText(_translate("MainWindow", "百亿项目组"))
        self.msgHistoryLabel.setText(_translate("MainWindow", "查看历史消息"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.16364pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.16364pt;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "此处输入文字...  "))
        self.pushBtn.setText(_translate("MainWindow", "发送"))


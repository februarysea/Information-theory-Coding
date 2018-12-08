# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import start

class Ui_page1_2(object):
    def setupUi(self, page1_2):
        page1_2.setObjectName("page1_2")
        page1_2.resize(400, 400)
        self.page = page1_2
        self.verticalLayoutWidget = QtWidgets.QWidget(page1_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 100, 311, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton_2 = QtWidgets.QPushButton(page1_2)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 290, 91, 35))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(page1_2)
        QtCore.QMetaObject.connectSlotsByName(page1_2)
        page1_2.setTabOrder(self.lineEdit, self.pushButton)
        page1_2.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, page1_2):
        _translate = QtCore.QCoreApplication.translate
        page1_2.setWindowTitle(_translate("page1_2", "Dialog"))
        self.label_2.setText(_translate("page1_2", "唯一可译码的判断"))
        self.label.setText(_translate("page1_2", "<html><head/><body><p>请在右侧输入符号数为4的任意编码：</p></body></html>"))
        self.pushButton.setText(_translate("page1_2", "确认"))
        self.label_3.setText(_translate("page1_2", "结果：等待确认"))
        self.pushButton_2.setText(_translate("page1_2", "返回"))

        self.pushButton_2.clicked.connect(self.jumpToStart)

    def jumpToStart(self):
        self.page.hide()


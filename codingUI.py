# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codingUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 70, 410, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.helloLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.helloLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.helloLabel.setTextFormat(QtCore.Qt.AutoText)
        self.helloLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helloLabel.setObjectName("helloLabel")
        self.verticalLayout.addWidget(self.helloLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName("button1")
        self.horizontalLayout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName("button2")
        self.horizontalLayout.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button3.setObjectName("button3")
        self.horizontalLayout.addWidget(self.button3)
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button4.setObjectName("button4")
        self.horizontalLayout.addWidget(self.button4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.helloLabel.setText(_translate("MainWindow", "请点击下列任意按钮开始实验"))
        self.button1.setText(_translate("MainWindow", "基础理论"))
        self.button2.setText(_translate("MainWindow", "信源编码方式"))
        self.button3.setText(_translate("MainWindow", "编码仿真"))
        self.button4.setText(_translate("MainWindow", "综合"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



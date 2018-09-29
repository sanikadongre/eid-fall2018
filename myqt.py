# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myqt.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 800)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Dialog.setMouseTracking(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(320, 20, 118, 23))
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.progressBar.setMouseTracking(True)
        self.progressBar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.progressBar.setProperty("value", 27)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 50, 113, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(320, 50, 118, 23))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.progressBar_2.setFont(font)
        self.progressBar_2.setMouseTracking(True)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 140, 301, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 150, 111, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 80, 201, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Temperature"))
        self.label_2.setText(_translate("Dialog", " Humidity"))
        self.label_3.setText(_translate("Dialog", "status"))
        self.label_4.setText(_translate("Dialog", "Date and Time"))


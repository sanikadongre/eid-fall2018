# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_login(object):
    def setupUi(self, user_login):
        user_login.setObjectName("user_login")
        user_login.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(user_login)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 171, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(user_login)
        self.label.setGeometry(QtCore.QRect(90, 40, 91, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(user_login)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(user_login)
        self.graphicsView.setGeometry(QtCore.QRect(230, 150, 131, 21))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(user_login)
        QtCore.QMetaObject.connectSlotsByName(user_login)

    def retranslateUi(self, user_login):
        _translate = QtCore.QCoreApplication.translate
        user_login.setWindowTitle(_translate("user_login", "Dialog"))
        self.label.setText(_translate("user_login", "Login name"))
        self.pushButton.setText(_translate("user_login", "Go"))


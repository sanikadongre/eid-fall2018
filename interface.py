# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myQT.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Display(object):
    def setupUi(self, Display):
        Display.setObjectName("Display")
        Display.resize(780, 390)
        Display.setEnablingNesting(False)
        #Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        #Dialog.setMouseTracking(False)
        self.optval = QtGui.QWidget(Display)
        self.optval = setObjectName(_fromUtf8("optval"))
        self.Timetag = (QtGui.QLabel(self.optval))
        self.Timetag.setGeometry(QtCore, QRect(330,165,64,16))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 191, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 151, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 80, 113, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 210, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 151, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 113, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(500, 80, 181, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(700, 80, 113, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(700, 140, 113, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 210, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(510, 140, 151, 31))
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 280, 901, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(110, 360, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(540, 360, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(190, 310, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(620, 310, 121, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 210, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")

       self.retranslateUi(DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow):
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "Temperature & Humidity Display ", None))
        self.Time_Label.setText(_translate("DisplayWindow", "Time", None))
        self.Time_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Temperature_Label.setText(_translate("DisplayWindow", "Temperature", None))
        self.Humidity_Label.setText(_translate("DisplayWindow", "Humidity", None))
        self.Humidity_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Temperature_Value.setText(_translate("DisplayWindow", "0.00", None))
        self.Refresh_PB.setText(_translate("DisplayWindow", "Refresh", None))
        self.alarm_display_label.setText(_translate("DisplayWindow", "Set Humidity Alarm", None))
        self.alarm_display_label_2.setText(_translate("DisplayWindow", "Set Temp Alarm", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TemperatureQT4.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
# Reference for csv file: https://stackabuse.com/reading-and-writing-csv-files-in-python/
#Reference for MQTT: https://opensource.com/article/18/6/mqtt

from PyQt5 import QtCore, QtGui, QtWidgets
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient as aws
import json
import os
from PyQt5.QtCore import QTimer
import Adafruit_DHT             #importing this to get the Adafruit DHT22 libraries
import sys
import socket
import ssl
import numpy
import datetime                 #importing this to get date and time of button push
import matplotlib.pyplot as pt1 #importing this to plot temperature and humidity graph
import matplotlib.pyplot as pt2
import matplotlib.pyplot as mplot
import csv

class Ui_TemperatureQT(object):

    def __init__(self):
        self.sum_humid = 0
        self.sum_temp = 0
        self.measure_count = 1
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.temp_unit = ' \u00b0' + 'C'
        self.max_temp = 0.0
        self.max_humid = 0.0
        self.min_temp = 50.0
        self.min_humid = 100.0
        self.all_temp = []              #creating an empty array so that data can be appended to it for graph plotting
        self.all_humidity = []

    def setupUi(self, TemperatureQT):
        TemperatureQT.setObjectName("TemperatureQT")
        TemperatureQT.resize(665, 403)
        TemperatureQT.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(TemperatureQT)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 61, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 132, 113, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 211, 61))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 180, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 231, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(290, 30, 81, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 80, 101, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(400, 20, 113, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 70, 113, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 130, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 130, 81, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 180, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 230, 101, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(400, 180, 113, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(400, 230, 113, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(300, 280, 81, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(400, 280, 113, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 330, 101, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(400, 330, 113, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        TemperatureQT.setCentralWidget(self.centralwidget)

        self.retranslateUi(TemperatureQT)
        self.getCurrTime()
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.storeData()
        self.timer = QTimer()
        self.timer.timeout.connect(self.getCurrTime)
        self.timer.timeout.connect(self.storeData)
        self.timer.timeout.connect(self.plotGraph)
        self.timer.start(5000)
        QtCore.QMetaObject.connectSlotsByName(TemperatureQT)

    def retranslateUi(self, TemperatureQT):
        _translate = QtCore.QCoreApplication.translate
        TemperatureQT.setWindowTitle(_translate("TemperatureQT", "TemperatureQT"))
        self.label.setText(_translate("TemperatureQT", "Temperature"))
        self.label_2.setText(_translate("TemperatureQT", "Humidity"))
        self.label_3.setText(_translate("TemperatureQT", "Time"))
        self.pushButton_2.setText(_translate("TemperatureQT", "Plot"))
        self.label_5.setText(_translate("TemperatureQT", "Error Message displayed below:"))
        self.label_6.setText(_translate("TemperatureQT", "Avg Temp"))
        self.label_7.setText(_translate("TemperatureQT", "Avg Humidity"))
        self.label_8.setText(_translate("TemperatureQT", "Temp Unit"))
        self.label_9.setText(_translate("TemperatureQT", "Min Temp"))
        self.label_10.setText(_translate("TemperatureQT", "Min Humidity"))
        self.label_11.setText(_translate("TemperatureQT", "Max Temp"))
        self.label_12.setText(_translate("TemperatureQT", "Max Humidity"))
        self.comboBox.addItem("Celsius")
        self.comboBox.addItem("Farhenite")
        self.pushButton_2.clicked.connect(self.plot_clicked)             #plot_clicked function will be called whenever 'Plot' button is clicked
        

         
    def storeData(self):
        #Function provided by Adafruit_DHT library for taking data from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(22,4)
        if humidity and temperature is not None:
            temp_data = '{0:.2f}'.format(temperature)
            humid_data = '{0:.2f}'.format(humidity)
            pydata = {'Temperature': temp_data, 'Humidity': humid_data}
            jsondata = json.dumps(pydata)
            mqtt_aws.publish(data_check, jsondata, 1)
            self.lineEdit.setText('{0:.2f}'.format((temperature*self.mult_factor)+ self.add_factor) + self.temp_unit)
            self.lineEdit_2.setText(humid_data  + '%')

            #Code for computing average of temperature and humidity values
            self.sum_humid += float(humidity)
            self.sum_temp += float(temperature)
            avg_humid = (self.sum_humid/float(self.measure_count))
            avg_temp = (self.sum_temp/float(self.measure_count))
            avg_temp_data = '{0:.2f}'.format(avg_temp)
            avg_humid_data = '{0:.2f}'.format(avg_humid)

            if self.measure_count==1:
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
            else:
                self.lineEdit_4.setText('{0:.2f}'.format((avg_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
                self.lineEdit_5.setText('{0:.2f}'.format(avg_humid) + '%')

            self.measure_count += 1
            if (temperature > self.max_temp):
                self.max_temp = temperature

            if (humidity > self.max_humid):
                self.max_humid = humidity

            if (temperature < self.min_temp):
                self.min_temp = temperature

            if (humidity < self.min_humid):
                self.min_humid = humidity

            max_temp_data = '{0:.2f}'.format(self.max_temp)
            min_temp_data = '{0:.2f}'.format(self.min_temp)
            max_humid_data = '{0:.2f}'.format(self.max_humid)
            min_humid_data = '{0:.2f}'.format(self.min_humid)
            self.lineEdit_8.setText('{0:.2f}'.format((self.max_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
            self.lineEdit_9.setText('{0:.2f}'.format(self.max_humid)+'%')

            self.lineEdit_6.setText('{0:.2f}'.format((self.min_temp*self.mult_factor)+self.add_factor)+self.temp_unit)
            self.lineEdit_7.setText('{0:.2f}'.format(self.min_humid)+'%')

            self.all_temp.append(temperature)                          
            self.all_humidity.append(humidity)                         

            #Writing acquired values to temphumid_data.csv file
            with open('temphumid_data.csv', 'a', newline = '') as comfile:
                file_write = csv.writer(comfile, delimiter = ',')
                file_write.writerow([humid_data, temp_data, avg_humid_data, avg_temp_data, max_humid_data, max_temp_data, min_humid_data, min_temp_data, self.getCurrTime()])


        
        else:
            with open('temphumid_data.csv', 'a', newline = '') as comfile:
                file_write = csv.writer(comfile, delimiter = ',')
                file_write.writerow([0, 0, 0, 0, 0, 0, 0, 0, self.getCurrTime()])
            print ("No Data Received; Try Again")
            self.label_4.setText("Error: Sensor not Connected")

    def getCurrTime(self):
        current = datetime.datetime.now()
        self.lineEdit_3.setText(current.strftime("%m/%d/%Y %H:%M:%S"))
        return current.strftime("%m/%d/%Y %H:%M:%S")

    def selectionchange(self):
        text = str(self.comboBox.currentText())
        if (text == "Farhenite"):
            self.mult_factor = 1.8
            self.add_factor = 32.0
            self.temp_unit = ' \u00b0' + 'F'
        else:
            self.mult_factor = 1.0
            self.add_factor = 0.0
            self.temp_unit = ' \u00b0' + 'C'



    #Function for plotting graph by pulling values from .csv file
    def plotGraph(self):
        x = []
        y = []
        with open('temphumid_data.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(float(row[0]))
                y.append(float(row[1]))
        i = range(0,len(x))
        fig1 = mplot.figure(1)
        mplot.plot(i,x,'b')
        mplot.title('Humidity Variation Graph')
        fig1.savefig('humid_plot.jpg')

        fig2 = mplot.figure(2)
        mplot.plot(i,y,'r')
        mplot.title('Temperature Variation Graph')
        fig2.savefig('temp_plot.jpg')

    def plot_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        if(len(self.all_temp)<10):                                      #show plot only in data collected points collected is more than 10
            self.label_4.setText(_translate("TemperatureQT","Error: Data not sufficient"))
            return
        i = range(0,len(self.all_temp))
        pt1.plot(i,self.all_temp)                         #plot temp data
        pt2.plot(i,self.all_humidity)                     #plot humidity data
        pt1.show()                                        #show temperature graph
        pt2.show()                                        #show humidity graph


if __name__ == "__main__":
    
    mqtt_aws = None
    name_client = "temperature_humidity"
    host = "abb1xpjvw6x95-ats.iot.us-east-1.amazonaws.com"
    rootCAPath = "./certificates2/AmazonRootCA1.pem"
    privateKeyPath = "./certificates2/f2de2b0af7-private.pem.key"
    certificatePath = "./certificates2/f2de2b0af7-certificate.pem.crt"
    data_check = "temphumid"
    mqtt_aws = aws(name_client)
    mqtt_aws.configureEndpoint(host,8883)
    mqtt_aws.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
    mqtt_aws.connect()
    app = QtWidgets.QApplication(sys.argv)
    TemperatureQT = QtWidgets.QMainWindow()
    ui = Ui_TemperatureQT()
    ui.setupUi(TemperatureQT)
    TemperatureQT.show()
    sys.exit(app.exec_())


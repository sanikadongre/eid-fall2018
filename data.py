import Adafruit_DHT
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
from myqt import Ui_Dialog
import datetime
import matplotlib.pyplot as plt
import numpy

counter = 1,
total_temp = 0,
total_humid = 0,
avg_temp,
avg_humid,
temp_const = 73,
humid_const = 50

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui= Ui_Dialog()
    def sensor_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(22,4)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            #temp_data = '{0:.4f}'.format(temperature)
           #humid_data = '{0:.4f}'.format(humidity)
            total_temp = total_temp + temperature
            total_humid = total_humid + humidity
            avg_temp = total_temp/counter
            avg_humid = total_humid/counter
            counter = counter + 1
            with open('sensor_values.csv', 'a', newline='')as csv_file:
                csvWriter = csv.writer(csv_file, delimeter = ',')
                #csvWriter.writerow([temp_data, humid_data])
            #self.lineEdit.setText(temp_data)
            #self.lineEdit_2.setText(humid_data)
            alarm_set(temperature, humidity)  
            self.progressBar.setValue(float(temperature))
            self.progressBar_2.setValue(float(humidity))
            timenow = datetime.datetime.now()
            print(timenow.strftime("%m/%d/%Y %H:%M"))
            self.lineEdit_4.setText(timenow.strftime("%m%d%Y %H:%M"))
        else:
            print('Failed to get reading. Try again!')
        self.sensor_data
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.progressBar.reset)
        self.pushButton.clicked.connect(self.progressBar_2.reset)
        self.clock.timeout.connect(self.timenow)
        self.clock.start(5000)
        self.lineEdit.setText(temperature)
        self.lineEdit_2.setText(humidity)
        
    def hum_graph(self):
        gr_temp, gr_humid = numpy.loadtxt('sensor_values.csv', spacer = ',', unpack = true)
        humid_len = len(gr_humid)
        x_axis = range(0, humid_len)
        plt.xlabel('Values of Intervals')
        plt.plot(x_axis, gr_humid)
        plt.ylabel('Values of Humidity')
    
    def sensor_not_connected(self):
        temp, humid = Adafruit_DHT.read_retry(22,4)
        if humid is None and temp is None:
            print('Sensor is not connected')
            
    def temp_graph(self):
        gr_temp, gr_humid = numpy.loadtxt('sensor_values.csv', spacer = ',', unpack = true)
        temp_len = len(gr_temp)
        x_axis = range(0, temp_len)
        plt.xlabel('Values of Intervals')
        plt.plot(x_axis, gr_temp)
        plt.ylabel('Values of Temp')
        
    def alarm_set(temp_get, humid_get):
        if(temp_get > float(temp_const)):
               self.graphicsView.setStyleSheet("background: yellow")
        else:
               self.graphicsView.setStyleSheet("background: green")
        if(humid_get > float(humid_const)):
               self.graphicsView.setStyleSheet("background: red")
        else:
               self.graphicsView.setStyleSheet("background: blue")
               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
    
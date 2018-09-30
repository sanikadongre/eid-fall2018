import Adafruit_DHT
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from version1_qt import Ui_Dialog
import datetime
import numpy

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.avg_humid=0
        self.avg_temp=0
        self.avg_counter=0
        self.temp_const= 40
        self.humid_const = 56
        self.separator = ','
    def sensor_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(22,4)
        if humidity is not None and temperature is not None:
            self.ui.lineEdit.setText('connected')
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            temp_data = '{0:.1f}'.format(temperature)
            humid_data = '{0:.1f}'.format(humidity)
            self.avg_temp = ((self.avg_temp) * self.avg_counter + temperature)/(self.avg_counter+1)
            self.avg_humid = ((self.avg_humid) * self.avg_counter  + humidity) / (self.avg_counter+1)
            self.avg_counter += 1
            self.ui.lcdNumber.display(temp_data)
            self.ui.lcdNumber_2.display(humid_data)
            self.ui.lcdNumber_3.display(self.avg_temp)
            self.ui.lcdNumber_4.display(self.avg_humid)
            #with open('sensor_values.csv', 'a', newline='')as csv_file:
              #  csvWriter = csv.writer(csv_file, self.separator)
               # csvWriter.writerow([temp_data, humid_data])
            if(temperature > (self.temp_const)):
               self.ui.graphicsView.setStyleSheet("background: red")
            else:
               self.ui.graphicsView.setStyleSheet("background: green")
            if(humidity > (self.humid_const)):
               self.ui.graphicsView_2.setStyleSheet("background: red")
            else:
               self.ui.graphicsView_2.setStyleSheet("background: green")
               

            timenow = datetime.datetime.now()
            print(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_2.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
        else:
            print('Failed to get reading. Please Try again!')
        
    def reset_but(self):
        self.ui.pushButton_2.clicked.connect(self.sensor_data)
          
                                           
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
            self.ui.lineEdit.setText('not connected')
    def temp_graph(self):
        gr_temp, gr_humid = numpy.loadtxt('sensor_values.csv', spacer = ',', unpack = true)
        temp_len = len(gr_temp)
        x_axis = range(0, temp_len)
        plt.xlabel('Values of Intervals')
        plt.plot(x_axis, gr_temp)
        plt.ylabel('Values of Temp')
     
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    xyz = AppWindow()
    xyz.sensor_data()
    xyz.reset_but()
    xyz.show()
    try:
        sys.exit(app.exec_())
    except:
        None
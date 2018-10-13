#Author: Sanika Dongre
#Date: 09/29/2018
#EID-PROJECT1
#Refrences: https://pythonspot.com/pyqt5
#reference for csv storage: https://realpython.com/python-csv
#pyqt official site for widget colour change
#pyqt tutorials
#reference for reading csv file in a list: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
#Reference for map plotting: https://www.youtube.com/watch?v=aS4WlOJQ4mQ
#Reference for date time https://docs.python.org/3/library/datetime.html
#Reference for user login window: https://stackoverflow.com/questions/11812000/login-dialog-pyqt

import Adafruit_DHT
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from version1_qt import Ui_Dialog
from login import Ui_user_login
from matplotlib.pyplot import *
from numpy import *
import datetime

#Login Window setup
class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.lu = Ui_user_login()
        self.lu.setupUi(self)
        self.lu.lineEdit.setText('Enter username here')
        self.show()
        self.lu.pushButton.clicked.connect(self.login)
        
        
    def login(self):
        None
        user_identity = self.lu.lineEdit.text()
        if((user_identity) != 'sanika'):
            self.lu.graphicsView.setStyleSheet("background: red")
        else:
            self.lu.graphicsView.setStyleSheet("background: green")
            self.accept()
           
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
        self.list_temp = []
        self.list_hum = []
        self.temp_max = 19.0
        self.temp_min = 1000.0
        self.humid_min = 101.0
        self.humid_max = 0.0
        try:
           #Reference: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
            with open('sensor_values.csv', 'r') as f:
                reader = csv.reader(f)
                list_read = list(reader)
        except:
            None
            #Finding running average of data read from csv file in list
        for k in list_read:
            self.list_temp.append(k[0])
            self.list_hum.append(k[1])
        
        for k in range(len(self.list_temp)):
            self.avg_temp = ((self.avg_temp) * self.avg_counter + float(self.list_temp[k]))/(self.avg_counter+1)
            self.avg_humid = ((self.avg_humid) * self.avg_counter + float(self.list_hum[k]))/(self.avg_counter+1)
            self.avg_counter+=1            
        
    def sensor_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(22,4,10,1)
        #Reading the temperature and humidity values
        if humidity is not None and temperature is not None:
            self.ui.lineEdit.setText('connected')
            humid_data = '{0:.1f}'.format(humidity)
            temp_data = '{0:.1f}'.format(temperature)
            self.ui.lcdNumber.display(temp_data)
            self.cel_unit = '\u00b0'+ 'C'
            self.ui.lineEdit_4.setText(self.cel_unit)
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            self.multiplication_factor = 1.8
            self.addition_factor = 32
            self.faran_unit = '\u00b0' + 'K'
            self.ui.pushButton_5.clicked.connect(self.temp_kelvin)
            self.avg_temp = ((self.avg_temp) * self.avg_counter + temperature)/(self.avg_counter+1)
            self.avg_humid = ((self.avg_humid) * self.avg_counter  + humidity) / (self.avg_counter+1)
            self.avg_counter += 1
            self.ui.lcdNumber_2.display(humid_data)
            self.ui.lcdNumber_3.display(self.avg_temp)
            self.ui.lcdNumber_4.display(self.avg_humid)
           # temp_k = (1.8 * temp_data + 32)
            #self.ui.lineEdit_3.setText('{0:.01f}'. format((temp_k))+ self.faran_unit)
            #To display the date and time in hours, minutes, seconds
            #https://docs.python.org/3/library/datetime.html
            timenow = datetime.datetime.now()
            print(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_2.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_5.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            if(self.temp_max < temperature):
                self.temp_max = temperature
            if(self.temp_min > temperature):
                self.temp_min = temperature
            if(self.humid_max < humidity):
                self.humid_max = humidity
            if(self.humid_min > humidity):
                self.humid_min = humidity
            self.ui.lcdNumber_6.display(self.temp_max)
            self.ui.lcdNumber_7.display(self.temp_min)
            timenow = datetime.datetime.now()
            self.ui.lineEdit_8.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_9.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            #reference for csv storage: https://realpython.com/python-csv
            #To store the data over n samples in a .csv file format
            with open('sensor_values.csv', 'a', newline='')as csv_file:
               csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
               csv_writer.writerow([temp_data, humid_data])
               timenow = datetime.datetime.now()
               self.ui.lineEdit_6.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
               self.ui.lineEdit_7.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            
            #Graph plot
            self.list_temp.append(temp_data)
            self.list_hum.append(humid_data)
            self.ui.pushButton_4.clicked.connect(self.hum_graph)
            self.ui.pushButton.clicked.connect(self.temp_graph)
            
            #pyqt official site for widget colour change
            #For Alarm Set
            if(temperature > (self.temp_const)):
               self.ui.graphicsView.setStyleSheet("background: red")
            else:
               self.ui.graphicsView.setStyleSheet("background: green")
            if(humidity > (self.humid_const)):
               self.ui.graphicsView_2.setStyleSheet("background: red")
            else:
               self.ui.graphicsView_2.setStyleSheet("background: green")
               
        else:
            #Data can't be read/ Sensor disconnected
            print('Failed to get reading. Please Try again!')
            print('Sensor is not connected')
            self.ui.lineEdit.setText('not connected')
            
    def temp_kelvin(self):
            hum_val, temp_val = Adafruit_DHT.read_retry(22,4,10,1)
            temp_k = (temp_val * self.multiplication_factor) + (self.addition_factor)
            self.ui.lcdNumber.display(temp_k)
            self.ui.lineEdit_4.setText(self.faran_unit)
            timenow = datetime.datetime.now()
            print(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_2.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.pushButton_3.clicked.connect(self.sensor_data)
        
    def reset_but(self):
        #reset button condition to get new values
        self.ui.pushButton_2.clicked.connect(self.sensor_data)
        
        #Reference for map plotting: https://www.youtube.com/watch?v=aS4WlOJQ4mQ   
                                           
    def hum_graph(self):
        #for displaying the graph for humidity values
        matplotlib.pyplot.plot(range(len(self.list_hum)), self.list_hum)
        matplotlib.pyplot.xlabel('Values of Intervals')
        matplotlib.pyplot.ylabel('Values of Humidity')
        matplotlib.pyplot.show()
           
            
    def temp_graph(self):
        #for displaying the graph for temperature values
        matplotlib.pyplot.plot(range(len(self.list_temp)), self.list_temp)
        matplotlib.pyplot.xlabel('Values of Intervals')
        matplotlib.pyplot.ylabel('Values of Temperature')
        matplotlib.pyplot.show()
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    xyz = AppWindow()
    user = LoginWindow()
    if user.exec_() == QtWidgets.QDialog.Accepted:
       xyz.sensor_data()
       xyz.reset_but()
       xyz.show()
       try:
           sys.exit(app.exec_())
       except:
           None

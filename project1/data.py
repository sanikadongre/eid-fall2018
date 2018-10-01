#Author: Sanika Dongre
#Date: 09/29/2018
#EID-PROJECT1
#Refrences: https://pythonspot.com/pyqt5
#reference for csv storage: https://realpython.com/python-csv
#pyqt official site for widget colour change
#pyqt tutorials

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
        if((user_identity) != 'sanika' or (user_identity) == 'SANIKA' or (user_identity) == 'Sanika'):
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
        try:
            with open('sensor_values.csv', 'r') as f:
                reader = csv.reader(f)
                list_read = list(reader)
        except:
            None
        for k in list_read:
            self.list_temp.append(k[0])
            self.list_hum.append(k[1])
        
        for k in range(len(self.list_temp)):
            self.avg_temp = ((self.avg_temp) * self.avg_counter + float(self.list_temp[k]))/(self.avg_counter+1)
            self.avg_humid = ((self.avg_humid) * self.avg_counter + float(self.list_hum[k]))/(self.avg_counter+1)
            self.avg_counter+=1            
        
    def sensor_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(22,4,10,0.1)
        #Reading the temperature and humidity values
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
            
            #To display the date and time in hours, minutes, seconds
            timenow = datetime.datetime.now()
            print(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            self.ui.lineEdit_2.setText(timenow.strftime("%m/%d/%Y %H:%M:%S"))
            
            #reference for csv storage: https://realpython.com/python-csv
            #To store the data over n samples in a .csv file format
            with open('sensor_values.csv', 'a', newline='')as csv_file:
               csv_writer = csv.writer(csv_file, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
               csv_writer.writerow([temp_data, humid_data])
            
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
            
        
    def reset_but(self):
        #reset button condition to get new values
        self.ui.pushButton_2.clicked.connect(self.sensor_data)
          
                                           
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
#Project3 : client.py
#Date created: 11/12/2018
#Reference links: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
#sqs: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html

import datetime
import matplotlib.pyplot as plt
import boto3
import ast
import matplotlib
import json
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def __init__(self):
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='temperature_humidity_data') #get queue by name
        self.max_temperature_data=[]
        self.min_temperature_data=[]
        self.present_temperature_data=[]
        self.avg_temperature_data=[]
        self.max_humidity_data=[]
        self.min_humidity_data=[]
        self.current_humidity_data=[]
        self.avg_humidity_data=[]
        self.readings = 0
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.unit = " C\n"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1316, 671)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.RequestData = QtWidgets.QPushButton(self.centralWidget)
        self.RequestData.setGeometry(QtCore.QRect(330, 200, 181, 121))
        self.RequestData.setAutoFillBackground(False)
        self.RequestData.setObjectName("RequestData")
        self.FahrenheitToCelcius = QtWidgets.QRadioButton(self.centralWidget)
        self.FahrenheitToCelcius.setGeometry(QtCore.QRect(60, 210, 100, 27))
        self.FahrenheitToCelcius.setObjectName("FahrenheitToCelcius")
        self.CtoFlabel = QtWidgets.QLabel(self.centralWidget)
        self.CtoFlabel.setGeometry(QtCore.QRect(30, 310, 210, 21))
        self.CtoFlabel.setObjectName("CtoFlabel")
        self.CelciusToFahrenhite = QtWidgets.QRadioButton(self.centralWidget)
        self.CelciusToFahrenhite.setGeometry(QtCore.QRect(60, 350, 100, 27))
        self.CelciusToFahrenhite.setObjectName("CelsiusToFahrenheit")
        self.FtoClabel = QtWidgets.QLabel(self.centralWidget)
        self.FtoClabel.setGeometry(QtCore.QRect(30, 180, 210, 21))
        self.FtoClabel.setObjectName("FtoClabel")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 211, 131))
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setIndent(35)
        self.label.setObjectName("label")
        self.MessageBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MessageBox.setGeometry(QtCore.QRect(760, 0, 540, 801))
        self.MessageBox.setObjectName("MessageBox")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(630, 260, 67, 21))
        self.label_2.setObjectName("label_2")
        self.ClearMessage = QtWidgets.QPushButton(self.centralWidget)
        self.ClearMessage.setGeometry(QtCore.QRect(600, 520, 151, 29))
        self.ClearMessage.setObjectName("ClearMessage")
        self.Close = QtWidgets.QPushButton(self.centralWidget)
        self.Close.setGeometry(QtCore.QRect(210, 520, 121, 31))
        self.Close.setObjectName("Close")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 14))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.Close.clicked.connect(MainWindow.close)
        self.ClearMessage.clicked.connect(self.MessageBox.clear)
        self.RequestData.clicked.connect(self.get_data)
        self.FahrenheitToCelcius.clicked.connect(self.fah_to_cel)
        self.CelciusToFahrenhite.clicked.connect(self.cel_to_fah)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RequestData.setText(_translate("MainWindow", "Get Data"))
        self.FahrenheitToCelcius.setText(_translate("MainWindow", "F to  C"))
        self.CtoFlabel.setText(_translate("MainWindow", "Celsius to Fahreinheit"))
        self.CelciusToFahrenhite.setText(_translate("MainWindow", "C to F"))
        self.FtoClabel.setText(_translate("MainWindow", "Fahreinheit to Celsius"))
        self.label.setText(_translate("MainWindow", "Temp Humid Graphical"))
        self.label_2.setText(_translate("MainWindow", "Output"))
        self.ClearMessage.setText(_translate("MainWindow", "Clear Data"))
        self.Close.setText(_translate("MainWindow", "Exit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))



    def get_data(self):
        queue_list = []
        for i in range(3):
            list_val = self.queue.receive_messages(MaxNumberOfMessages=10) # Receive 10 messages
            if not list_val:
                break
            for msg in list_val:
                msgbody = ast.literal_eval(msg.body)  # Appending of data
                queue_list.append(msgbody)
                msg.delete()    # To delete the msg
                self.readings += 1

       
        if queue_list:
            for mesg in queue_list:
                self.present_temperature_data.append(mesg["curr_temp"])
                self.current_humidity_data.append(mesg["curr_humid"])
                self.max_temperature_data.append(mesg["max_temp"])
                self.max_humidity_data.append(mesg["max_humid"])
                self.min_temperature_data.append(mesg["min_temp"])
                self.min_humidity_data.append(mesg["min_humid"])
                self.avg_temperature_data.append(mesg["avg_temp"])
                self.avg_humidity_data.append(mesg["avg_humid"])

            output=""
            for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(self.max_temperature_data,\
                self.min_temperature_data,self.present_temperature_data, self.avg_temperature_data, self.max_humidity_data,\
                self.min_humidity_data, self.current_humidity_data, self.avg_humidity_data):


                output+= "Last Temp: {0:.2f}".format((curr_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Last Hum: "+ str(curr_h) + " %\n" + \
                                "Max Temp: {0:.2f}".format((max_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Max Hum: "+ str(max_h) + " %\n" + \
                                "Min Temp: {0:.2f}".format((min_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Min_Hum: "+str(min_h) + "%\n" + \
                                "Avg Temp: {0:.2f}".format((avg_t*self.mult_factor)+self.add_factor) + self.unit + \
                                "Avg Hum: "+ str(avg_h) + " %\n\n"
            self.MessageBox.setText("Obtained Data:\n"  + output + "\nTimestamp: " + str(datetime.datetime.now()))
            self.plotGraph()
        # Error Handling
        else:
            self.MessageBox.setText("Error Fetching Data \n")
            
    # Unit conversion
    def cel_to_fah(self):
        self.mult_factor = 1.8
        self.add_factor = 32.0
        self.unit = " F\n"

    def fah_to_cel(self):
        self.mult_factor = 1.0
        self.add_factor = 0.0
        self.unit = " C\n"


    # Function for plotting graph of humidity and temperature separately
    def plotGraph(self):
        plt.plot(range(self.readings), self.max_temperature_data, 'r-', label='Max Temp')  #red
        plt.plot(range(self.readings), self.min_temperature_data, 'b-', label='Min Temp')  #blue
        plt.plot(range(self.readings), self.present_temperature_data, 'g-', label='Last Temp')  #green
        plt.plot(range(self.readings), self.avg_temperature_data, 'y-', label='Avg Temp')  #yellow
        plt.legend(loc='best')
        plt.title('Temperature Graph')
        plt.ylabel('Temperature Celsius')
        plt.xlabel('readings')
        plt.show()
        plt.plot(range(self.readings), self.max_humidity_data, 'r-', label='Max Hum')  #red
        plt.plot(range(self.readings), self.min_humidity_data, 'b-', label='Min Hum')  #blue
        plt.plot(range(self.readings), self.current_humidity_data, 'g-', label='Last Hum') #green
        plt.plot(range(self.readings), self.avg_humidity_data, 'y-', label='Avg Hum') #yellow
        plt.legend(loc='best')
        plt.title('Humidity Graph')
        plt.ylabel('Humidity %')
        plt.xlabel('Number of readings')
        plt.show()

  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



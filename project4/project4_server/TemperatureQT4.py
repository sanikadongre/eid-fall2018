# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TemperatureQT4.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
# Reference for csv file: https://stackabuse.com/reading-and-writing-csv-files-in-python/
from PyQt5 import QtCore, QtGui, QtWidgets
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient as aws
import json
import os
import paho.mqtt.client as mqtt #for mqtt
import aiocoap.resource as resource
from PyQt5.QtCore import QTimer
import Adafruit_DHT             #importing this to get the Adafruit DHT22 libraries
import sys
import socket
import pika #for amqp
import aiocoap #for coap
import ssl
import asyncio
import threading
import numpy
import datetime                 #importing this to get date and time of button push
import tornado.httpserver
import tornado.websocket #for websockets
import tornado.ioloop
import tornado.web
import matplotlib.pyplot as pt1 #importing this to plot temperature and humidity graph
import matplotlib.pyplot as pt2
import matplotlib.pyplot as mplot
import csv

class Ui_TemperatureQT(object):

    def __init__(self):
        self.add_humidity = 0
        self.add_temperature = 0
        self.count_values = 1
        self.multiplication_indicator = 1.0
        self.addition_indicator = 0.0
        self.temp_unit = ' \u00b0' + 'C'
        self.maximum_temp = 0.0
        self.maximum_humidity = 0.0
        self.minimum_temp = 50.0
        self.minimum_humidity = 100.0
        

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
        self.presenttimecalc()
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.storeData()
        self.timer = QTimer()
        self.timer.timeout.connect(self.presenttimecalc)
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
       # self.pushButton_2.clicked.connect(self.plot_clicked)             #plot_clicked function will be called whenever 'Plot' button is clicked
         
    def storeData(self):
        #Function provided by Adafruit_DHT library for taking data from DHT22 sensor
        humidity, temperature = Adafruit_DHT.read_retry(22,4)
        if humidity and temperature is not None:
            temp_data = '{0:.2f}'.format(temperature)
            humid_data = '{0:.2f}'.format(humidity)
            pydata = {'Temperature': temp_data, 'Humidity': humid_data}
            jsondata = json.dumps(pydata)
            mqtt_aws.publish(data_check, jsondata, 1)
            self.lineEdit.setText('{0:.2f}'.format((temperature*self.multiplication_indicator)+ self.addition_indicator) + self.temp_unit)
            self.lineEdit_2.setText(humid_data  + '%')
            #Code for computing average of temperature and humidity values
            self.add_humidity += float(humidity)
            self.add_temperature += float(temperature)
            avg_humid = (self.add_humidity/float(self.count_values))
            avg_temp = (self.add_temperature/float(self.count_values))
            avg_temp_data = '{0:.2f}'.format(avg_temp)
            avg_humid_data = '{0:.2f}'.format(avg_humid)
            if self.count_values==1:
                self.lineEdit_4.setText("")
                self.lineEdit_5.setText("")
            else:
                self.lineEdit_4.setText('{0:.2f}'.format((avg_temp*self.multiplication_indicator)+self.addition_indicator)+self.temp_unit)
                self.lineEdit_5.setText('{0:.2f}'.format(avg_humid) + '%')

            self.count_values += 1
            if (temperature > self.maximum_temp):
                self.maximum_temp = temperature

            if (humidity > self.maximum_humidity):
                self.maximum_humidity = humidity

            if (temperature < self.minimum_temp):
                self.minimum_temp = temperature

            if (humidity < self.minimum_humidity):
                self.minimum_humidity = humidity
            maximum_temp_data = '{0:.2f}'.format(self.maximum_temp)
            minimum_temp_data = '{0:.2f}'.format(self.minimum_temp)
            maximum_humidity_data = '{0:.2f}'.format(self.maximum_humidity)
            minimum_humidity_data = '{0:.2f}'.format(self.minimum_humidity)
            self.lineEdit_8.setText('{0:.2f}'.format((self.maximum_temp*self.multiplication_indicator)+self.addition_indicator)+self.temp_unit)
            self.lineEdit_9.setText('{0:.2f}'.format(self.maximum_humidity)+'%')
            self.lineEdit_6.setText('{0:.2f}'.format((self.minimum_temp*self.multiplication_indicator)+self.addition_indicator)+self.temp_unit)
            self.lineEdit_7.setText('{0:.2f}'.format(self.minimum_humidity)+'%')                
            #Writing acquired values to temphumid_data.csv file
            with open('temphumid_data.csv', 'a', newline = '') as comfile:
                writeoperation = csv.writer(comfile, delimiter = ',')
                writeoperation.writerow([humid_data, temp_data, avg_humid_data, avg_temp_data, maximum_humidity_data, maximum_temp_data, minimum_humidity_data, minimum_temp_data, self.presenttimecalc()])
        else:
            with open('temphumid_data.csv', 'a', newline = '') as comfile:
                writeoperation = csv.writer(comfile, delimiter = ',')
                writeoperation.writerow([0, 0, 0, 0, 0, 0, 0, 0, self.presenttimecalc()])
            print ("No Data Received; Try Again")
            self.label_4.setText("Error: Sensor not Connected")

    def presenttimecalc(self):
        current = datetime.datetime.now()
        self.lineEdit_3.setText(current.strftime("%m/%d/%Y %H:%M:%S"))
        return current.strftime("%m/%d/%Y %H:%M:%S")

    def selectionchange(self):
        text = str(self.comboBox.currentText())
        if (text == "Farhenite"):
            self.multiplication_indicator = 1.8
            self.addition_indicator = 32.0
            self.temp_unit = ' \u00b0' + 'F'
        else:
            self.multiplication_indicator = 1.0
            self.addition_indicator = 0.0
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

#resouce blocking coap
class resources_block(resource.Resource):

    def set_content(self, content):
        self.content = content

    async def render_put(self, request):
       self.set_content(request.payload)
       return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)
    
#system configurations
def System_UI():
    app = QtWidgets.QApplication(sys.argv)
    TemperatureQT = QtWidgets.QMainWindow()
    ui = Ui_TemperatureQT()
    ui.setupUi(TemperatureQT)
    TemperatureQT.show()
    sys.exit(app.exec_())
    
#coap server
def Coap_server():
    loop_func = asyncio.new_event_loop()
    asyncio.set_event_loop(loop_func)
    root = resource.Site()
    root.add_resource(('.well-known', 'core'),
           resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(('other', 'block'), resources_block())
    asyncio.Task(aiocoap.Context.create_server_context(root))
    loop_func = asyncio.get_event_loop()
    loop_func.run_forever()
    
#mqtt function server side using mosquitto broker
def func_mqtt():
    client = mqtt.Client()
    client.connect("test.mosquitto.org",1883,60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(up_topic)

def on_message(client, userdata, msg):
    client.publish(down_topic, msg.payload);

#websocketshandler for websockets
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection for websocket started')

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print ('connection for websocket closed')

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler)])

#websock server function
def websocket_server():
    http_server = tornado.httpserver.HTTPServer(application)
    ip_addr = '127.0.0.1' 
    port = 8888 #port
    http_server.listen(port, address='10.0.0.203') #ip address
    print ('The Websocket server started at %s' % ip_addr)
    tornado.ioloop.IOLoop.instance().start()
    
#function for rabbitmq server
def rabbitmq_server():
    channel.queue_declare(queue='up_queue') #upqueue
    channel.basic_consume(callback,queue='up_queue', no_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    channel.queue_declare(queue='down_queue') #downqueue
    channel.basic_publish(exchange='', routing_key='down_queue', body= body )
        
if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) #connection using localhost
    channel = connection.channel()
    mqtt_aws = None
    name_client = "temperature_humidity"
    host = "abb1xpjvw6x95-ats.iot.us-east-1.amazonaws.com"
    rootCAPath = "./certificates2/AmazonRootCA1.pem"
    privateKeyPath = "./certificates2/f2de2b0af7-private.pem.key"
    certificatePath = "./certificates2/f2de2b0af7-certificate.pem.crt"
    data_check = "temphumid"
    mqtt_aws = aws(name_client)
    up_topic = 'mqtt_upstream'
    down_topic = 'mqtt_downstream'
    mqtt_aws.configureEndpoint(host,8883)
    mqtt_aws.configureCredentials(rootCAPath, privateKeyPath, certificatePath)
    mqtt_aws.connect()
    calcthread = [] #threads for executing code parallely
    thread_ui = threading.Thread(target=System_UI)
    calcthread.append(thread_ui)
    thread_ui.start() 
    coapthread = threading.Thread(target=Coap_server)
    calcthread.append(coapthread)
    coapthread.daemon = True
    coapthread.start() #coap thread
    mqtt_thread = threading.Thread(target=func_mqtt)
    calcthread.append(mqtt_thread)
    mqtt_thread.daemon = True
    mqtt_thread.start() #mqtt thread
    threadwebsocket = threading.Thread(target=websocket_server)
    calcthread.append(threadwebsocket)
    threadwebsocket.daemon = True
    threadwebsocket.start() #websockets thread
    rabbitmq_thread = threading.Thread(target=rabbitmq_server)
    calcthread.append(rabbitmq_thread)
    rabbitmq_thread.daemon = True
    rabbitmq_thread.start() #rabbitmq thread

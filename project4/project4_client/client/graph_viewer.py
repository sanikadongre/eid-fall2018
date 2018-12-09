#Project4: graph_viewer.py
#Date created: 11/12/2018
#Reference links: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
#sqs: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html
import datetime
from websocket import create_connection
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
import boto3
import ast
from aiocoap import *
import matplotlib
import json
import threading
import sys
import asyncio
import time
from PyQt5 import QtCore, QtGui, QtWidgets
    
class Ui_MainWindow(object):

    def __init__(self):
        self.sqs = boto3.resource('sqs')
        self.queue = self.sqs.get_queue_by_name(QueueName='temperature_humidity_data') #get queue by name
        self.present_temperature_data=[]
        self.present_humidity_data=[]
        self.max_temperature_data=[]
        self.max_humidity_data=[]
        self.min_temperature_data=[]
        self.min_humidity_data=[]
        self.avg_temperature_data=[]
        self.avg_humidity_data=[]
        self.readings = 0
        self.multiplication_indicator = 1.0
        self.addition_indicator = 0.0
        self.unit = '\u00b0' + 'C'
        self.websockets_time=[]
        self.output=""
        self.coap_time=[]
        self.mqtt_time=[]
        self.message_num=[]
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1316, 671)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.getdata_3 = QtWidgets.QPushButton(self.centralWidget)
        self.getdata_3.setGeometry(QtCore.QRect(330, 200, 181, 121))
        self.getdata_3.setObjectName("getdata_3")               
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 211, 131))
        self.label.setObjectName("label")
        self.MessageBox = QtWidgets.QTextEdit(self.centralWidget)
        self.MessageBox.setGeometry(QtCore.QRect(760, 0, 540, 801))
        self.MessageBox.setObjectName("MessageBox")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(630, 260, 67, 21))
        self.label_2.setObjectName("label_2")
        self.ClearMessage = QtWidgets.QPushButton(self.centralWidget)
        self.ClearMessage.setGeometry(QtCore.QRect(210, 520, 121, 31))
        self.ClearMessage.setObjectName("ClearMessage")
        self.Close = QtWidgets.QPushButton(self.centralWidget)
        self.Close.setGeometry(QtCore.QRect(600, 520, 151, 29))
        self.Close.setObjectName("Close")
        self.getdata = QtWidgets.QPushButton(self.centralWidget)
        self.getdata.setGeometry(QtCore.QRect(330, 150, 180, 40))
        self.getdata.setObjectName("getdata")
        self.getdata_2 = QtWidgets.QPushButton(self.centralWidget)
        self.getdata_2.setGeometry(QtCore.QRect(330, 330, 180, 40))
        self.getdata_2.setObjectName("getdata_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.Close.clicked.connect(MainWindow.close)
        self.ClearMessage.clicked.connect(self.MessageBox.clear)
        self.getdata_3.clicked.connect(self.get_data)
        self.getdata.clicked.connect(self.plotGraph)
        self.getdata_2.clicked.connect(self.time_protocols)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.getdata_3.setText(_translate("MainWindow", "Get Data"))
        self.label.setText(_translate("MainWindow", "Temp Humid Graphical"))
        self.label_2.setText(_translate("MainWindow", "Results"))
        self.ClearMessage.setText(_translate("MainWindow", "Clear Data"))
        self.Close.setText(_translate("MainWindow", "Exit"))
        self.getdata.setText(_translate("MainWindow", "Graph view"))
        self.getdata_2.setText(_translate("MainWindow", "Protocols"))
            
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
                self.present_humidity_data.append(mesg["curr_humid"])
                self.max_temperature_data.append(mesg["max_temp"])
                self.max_humidity_data.append(mesg["max_humid"])
                self.min_temperature_data.append(mesg["min_temp"])
                self.min_humidity_data.append(mesg["min_humid"])
                self.avg_temperature_data.append(mesg["avg_temp"])
                self.avg_humidity_data.append(mesg["avg_humid"])
            for max_t,min_t,curr_t,avg_t,max_h,min_h,curr_h,avg_h in zip(self.max_temperature_data,\
                self.min_temperature_data,self.present_temperature_data, self.avg_temperature_data, self.max_humidity_data,\
                self.min_humidity_data, self.present_humidity_data, self.avg_humidity_data):
                self.output+= "Last Temp: {0:.2f}".format((curr_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n"+ \
                                "Last Hum: "+ str(curr_h) + " %\n" + \
                                "Max Temp: {0:.2f}".format((max_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n"+ \
                                "Max Hum: "+ str(max_h) + " %\n" + \
                                "Min Temp: {0:.2f}".format((min_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n" + \
                                "Min_Hum: "+str(min_h) + "%\n" + \
                                "Avg Temp: {0:.2f}".format((avg_t*self.multiplication_indicator)+self.addition_indicator) + self.unit + "\n" + \
                                "Avg Hum: "+ str(avg_h) + " %\n\n"
            self.MessageBox.setText("Obtained Data:\n"  + self.output + "\nTimestamp: " + str(datetime.datetime.now()))
            #self.plotGraph()
        #error check
        else:
            self.MessageBox.setText("Error Fetching Data \n")
            
    def time_protocols(self):
        self.get_data()
        web_time1 = time.time()
        self.web_client()
        web_time2 = time.time()
        web_execution_time = web_time2 - web_time1
        self.websockets_time.append(web_execution_time)
        print('\nThe exchange time for Websocket is: %s'% web_execution_time)
        print('\nnumber messages: %d'% self.readings)
        print("\nThe CoAP output:\n")
        coapthread = threading.Thread(target=self.coap_collect)
        coap_time1 = time.time()
        coapthread.start()
        coapthread.join()
        coap_time2 = time.time()
        coap_execution_time = (coap_time2 - coap_time1)
        self.coap_time.append(coap_execution_time)
        print('\nThe exchange time for CoAP is: %s'% coap_execution_time)
        print('\nnumber of messages: %d'% self.readings)
        mqtt_time1 = time.time()
        client.publish(up_topic, self.output)
        msg_event.wait()
        mqtt_time2 = time.time()
        mqtt_execution_time = (mqtt_time2 - mqtt_time1)
        msg_event.clear()
        self.mqtt_time.append(mqtt_execution_time)
        print('\nThe exchange time for MQTT is: %s seconds'% mqtt_execution_time)
        print('\nnumber of messages: %d'% self.readings)
        self.message_num.append(self.readings)
        self.plotoutputprotocol()

    
    # Function for plotting graph of humidity and temperature separately
    def plotGraph(self):
        self.get_data()
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
        plt.plot(range(self.readings), self.present_humidity_data, 'g-', label='Last Hum') #green
        plt.plot(range(self.readings), self.avg_humidity_data, 'y-', label='Avg Hum') #yellow
        plt.legend(loc='best')
        plt.title('Humidity Graph')
        plt.ylabel('Humidity %')
        plt.xlabel('Number of readings')
        plt.show()
        
    def plotoutputprotocol(self):
        plt.plot(self.message_num, self.websockets_time, 'g-', label='P1: WebSocket')
        plt.plot(self.message_num, self.coap_time, 'r-', label='P2: CoAP')
        plt.plot(self.message_num, self.mqtt_time, 'b-', label='P3: MQTT')
        #plt.plot(self.num_messages_list, self.amqp_time_list, 'g-', label='Rabbit AMQP')
        plt.legend(loc='best')
        plt.title('Protocol comparison')
        plt.ylabel('Transfer time of protocol')
        plt.xlabel('Messages number')
        plt.show()
        
    def web_client(self):
        ws.send(self.output)
        websocket_output =  ws.recv()
        print("\nwebsocket data:\n")
        print(websocket_output)
        
    async def coapPUT(self, data):
        context = await Context.create_client_context()
        await asyncio.sleep
        request = Message(code=PUT, payload=bytes(data, 'utf-8'))
        request.opt.uri_host = "10.0.0.203"
        request.opt.uri_path = ("other", "block")
        response = await context.request(request).response
        print('The response output is: %s\n%r'%(response.code, response.payload))
    
    def coap_collect(self):
        loop_func = asyncio.new_event_loop()
        asyncio.set_event_loop(loop_func)
        loop_func = asyncio.get_event_loop()
        loop_func.run_until_complete(self.coapPUT(self.output))
        return 0
    
def func_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(down_topic)


def on_message(client, userdata, msg):
    print(str(msg.payload))
    msg_event.set()

if __name__ == "__main__":
    ws = create_connection("ws://10.0.0.203:8888/ws")
    msg_event = threading.Event()
    up_topic = 'mqtt_upstream'
    down_topic = 'mqtt_downstream'
    client = mqtt.Client()
    client.connect('test.mosquitto.org',1883,60)
    calcthread = []
    mqttthread = threading.Thread(target=func_mqtt)
    calcthread.append(mqttthread)
    mqttthread.daemon = True
    mqttthread.start()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



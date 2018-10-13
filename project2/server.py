import tornado.websocket
from tornado.websocket import *
import tornado.ioloop
import tornado.web
from matplotlib.pyplot import *
import numpy
import tornado.httpserver
import csv
import datetime
import socket

class WSHandler(tornado.websocket.WebSocketHandler):
    def open_sock(self):
        print('The setup connection')
    def msg_send_recv(self):
        print('client request: %s' %msg)
        self.write_message(msg + '-' + str(database(msg)))
    def close_sock(self):
        print('The connection is closed')
    def check_condition(self):
        return True
    application = tornado.web.Application([
        (r'/ws', WSHandler),
        (r"/(humidity_plot.jpg)", tornado.web.StaticFileHandler, {'path':'./'}),
        (r"/(temperature_plot.jpg)", tornado.web.StaticFileHandler, {'path':'./'})
    ])
                                                                                                                                                                                              
    def data_sensor(msg):
        get_csv_file = open('sensor_values.csv', 'r')
        end = get_csv_file.readlines()[-1]
        temp_get = end.split(",")
        if(temp_get[0] == 0 or temp_get[2] == 0 or temp_get[4] == 0 or temp_get[6] == 0 or temp_get[8] == 0 or temp_get[5] == 0 or temp_get[10] == 0 or temp_get[12] == 0 or temp_get[14] == 0 or temp_get[1] == 0 or temp_get[3] == 0 or temp_get[5] == 0 or temp_get[7] == 0 or temp_get[9] == 0 or temp_get[11] == 0 or temp_get[13] == 0 or temp_get[15] == 0):
            return 'ERROR'
        if(msg == 'present_temp'):
            return temp_get[0] + '-' + temp_get[1] + 'hours'
        elif (msg == 'present_humidity'):
            return temp_get[2] + '-' + temp_get[3] + 'hours'
        elif (msg == 'avg_temp'):
            return temp_get[4] + '-' + temp_get[5] + 'hours'
        elif (msg == 'avg_humid'):
            return temp_get[6] + '-' + temp_get[7] + 'hours'
        elif (msg == 'Max_temp'):
            return temp_get[8] + '-' + temp_get[9] + 'hours'
        elif (msg == 'Max_humid'):
            return temp_get[10] + '-' + temp_get[11] + 'hours'
        elif (msg == 'Min_temp'):
            return temp_get[12] + '-' + temp_get[13] + 'hours'
        elif (msg == 'Min_humid'):
            return temp_get[14] + '-' + temp_get[15] + 'hours'
        elif (msg == 'graph_humidity'):
            return humidity_url
        elif (msg == 'graph_temperature'):
            return temperature_url
        else:
            return 'The input is invalid'
        
if __name__ == "__main__":
    server = tornado.httpserver.HTTPServer(application)
    ip = '10.0.0.224'
    port = 8888
    humidity_url = 'http://' + ip + ':' + str(port) + '/humidity_plot.jpg'
    temperature_url = 'http://' + ip + ':' + str(port) + '/temperature_plot.jpg'
    server.listen(8888, address= '10.0.0.224')
    print(' *** Websocket Server Started at %s***' %ip)
    tornado.ioloop.IOLoop.instance().start()
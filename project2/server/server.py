import tornado.websocket
import tornado.ioloop
import tornado.web
from matplotlib.pyplot import *
import numpy
import csv
import datetime
import socket

class WSHandler(tornado.websocket.WebsocketHandler):
    def open_sock(self):
        print('The setup connection')
    def msg_send_recv(self):
        print('client request: %s' %msg)
        self.write_message(msg + '-' + str(database(msg)))
    def close
                    

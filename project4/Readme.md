Project4
Communication Protocol Comparison
The round trip times for transferring message from client back to client via server for IoT protocols: MQTT, COAP  Websockets and AMQP are compared. 
Description: 
Server: The DHT22 sensor is connected to Raspberry pi. The output of the sensor (temperature and humidity) can be observed in the QT GUI. This server data is sent to AWS using the AWS IOT Python SDK and a lambda function (lambda.js) is used to calculate the maximum, minimum and average readings for temperature and humidity. This data is added into SQS queue. The data from SQS queue is fetched using the boto3 library on the client raspberry pi. The Client QT GUI displays graph for 30 readings  for humidity and temperature (Maximum,Minimum,Current and average readings). A button on the GUI displays a graph comparing the protocols: MQTT, Coap, Websockets and AMQP (partially implemented using localhost) for the execution time vs the messages sent.
Protocols Implemented:
CoAP, Websockets, MQTT using mosquito broker and RabbitMQ using queue. 
Extra Credit:
RabbitMQ for localhost. 
To run the code:
 Run TemperatureQT4.py on the server side
And graph_viewer.py on the client side. Press ‘Get Data’ to get the current data and ‘protocols’ button on client QT interface to observe the graphs for 4 protocols. 
Installation required:
1)	pip install AWSIoTPythonSDK
2)	sudo pip3 aws cli
3)	pip install boto3
4)	Installation of asyncio, tornado, aiocoap, pika, paho-mqtt and mosquito
References:
1)	https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html - To view the messages in monitor on AWS and test in AWS.
2)	https://www.youtube.com/watch?v=y6W9QfiEY2E&t=4s – Registering a thing and observing in test (AWS)
3)	https://www.youtube.com/watch?v=Phzzk-cdF-g&t=400 – Creating lambda rule youtube
4)	https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html - To create lambda rule
5)	https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html - For fetching the data using boto3
6)	https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html - IAM account creation and adding user to group and getting credentials.
7)	https://os.mbed.com/cookbook/Websockets-Server - Websockets server example
8)	http://www.steves-internet-guide.com/into-mqtt-python-client/ -mqtt protocol
9)	https://mosquitto.org – broker for mqtt
10)	https://pypi.org/project/paho-mqtt/ - paho mqtt client
11)	https://www.switchdoc.com/2018/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/ - using mosquitto as a broker
12)	https://aiocoap.readthedocs.io/en/latest/examples.html - aiocoap for implementing coap protocol
13)	https://www.rabbitmq.com/tutorials/tutorial-one-python.html - rabbitmq protocol



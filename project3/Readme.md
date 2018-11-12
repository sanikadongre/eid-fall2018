Project 3 – AWS – MQTT

Individual project by – SANIKA DONGRE


In this project, both the client and server rpis are interfaced to QT GUI. The sensor side rpi is connected to the DHT22 sensor. The data is sent to the AWS in a JSON format. The library used for this purpose is: AWS-IOT-PYTHON-SDK. In the AWS first, a thing is created and it gets data from server side which can be viewed by test option in AWS. The lambda function is used to calculate 8 values (Min, Max, Latest, Average for temperature and humidity respectively). The lambda function is linked with thing using two rules pick_temperature and pick_humidity. The SQS queue is created and by creating a role the lambda function data is sent to the SQS queue. The data from the Queue is fetched by making use of credentials found in IAM account and using the boto library. The data fetched from the queue is displayed on the client-side QT interface. This client-side QT interface displays 4-line graphs for Max, Min, Current and Average readings for temperature and humidity). The data is displayed for over last 30 values and the graph lines are clearly labeled and distinguished using colors. 

The server file is: TemperatureQT4.py
and the client file is: client.py

Project References: 
https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html - To view the messages in monitor on AWS and test in AWS. 

https://www.youtube.com/watch?v=y6W9QfiEY2E&t=4s – Registering a thing and observing in test (AWS)

https://www.youtube.com/watch?v=Phzzk-cdF-g&t=400 – Creating lambda rule youtube

https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html - To create lambda rule

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html - For fetching the data using boto3

https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html - IAM account creation and adding user to group and getting credentials.








import Adafruit_DHT
import datetime

humidity, temperature = Adafruit_DHT.read_retry(22,4)
if humidity is not None and temperature is not None:
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        timenow = datetime.datetime.now()
        print(timenow.strftime("%m/%d/%Y %H:%M"))
else:
        print('Failed to get reading. Try again!')
    
    
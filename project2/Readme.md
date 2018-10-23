# Embedded Interface Design
# Project 2: Server Client Websocket connection
# Authors: Shubham Jaiswal and Sanika Dongre
# University of Colorado Boulder  
The Project contains:
1.User Interface(.ui) file.
2.A python script which uses pyqt5 libraries to render UI.
3.An html file that creates the webpage on Client pi.
4.Server.py file that establishes the websocket handshaking and fetches the data from .csv file.
5. A .csv file is created as a database for storing the obtained values from the sensor.
How to Run the Code:Clone the git repository to your Raspberry Pi. Go to folder Project2 run the TemperatureQT4.py script by typing in the terminal "python3 TemperatureQT4.py" Then the GUI will Appear.
The temperature, humidity,average temperature,average humidity,Minimum and Maximum temperature and Minimum and Maximum Humidity and time data is shown in the UI.
Plot button will plot the temperature and humidity data on two separate graphs. The graph will be ploteed only if the no of data points collected is greater than 10 and if not then an error message will be displayed.
The HTML page for the client displays all the mandatory 8 buttons for requesting the sensor data and a few additional ones as well.

**Instructions to run the code:**  
#check the IP caddress before using and change it if nedded.
1. run TemperatureQT4.py which interacts with the sensors and stores the data in the database(a csv). Command: python3 TemperatureQT4.py
2. Start the server by running the following command: python server.py
3. start webpage by clicking on the client.html file. file will open up in a browser and connect to server.
4. The page is then self-explanatory for its functioning.

**References:**  
 https://www.w3schools.com/html/default.asp
 https://www.w3schools.com/css/default.asp
 https://www.w3schools.com/jquery/default.asp
 https://www.w3schools.com/js/default.asp
 https://os.mbed.com/cookbook/Websockets-Server

 




//Homework-4: Author: Sanika Dongre
//Reference: https://github.com/momenso/node-dht-sensor
//Timeout reference: https://www.w3schools.com/jsref/met_win_settimeout.asp
//Javascript reference: sololearn nodejs android application


var sensor = require('node-dht-sensor');

var count=0;
var humid_max=0.0;
var temp_max=-100.0;
var temp_min=1000.0;
var humid_min=101.0;
var temp_avg=0.0;
var humid_avg=0.0;
var counter=0;
var temperature_temp=0;
var humidity_temp=0;

function ht_read()
{
	sensor.read(22, 4, function(err,temperature, humidity)
	{
			temp_now=1.8*temperature.toFixed(2)+32;
			humid_now=1*humidity.toFixed(2)+0;
			if(humid_max<humid_now)
			{
				humid_max=humid_now;
			}
			if(humid_min>humid_now)
			{
				humid_min=humid_now;
			}
			if(temp_max<temp_now)
			{
				temp_max=temp_now;
			}
			if(temp_min>temp_now)
			{
				temp_min=temp_now;
			}
			temperature_temp = Math.round(temp_avg*counter);
			humidity_temp = Math.round(humid_avg*counter);
			temp_avg = parseFloat(((temperature_temp+temp_now)/(counter+1)).toFixed(2));
			humid_avg = parseFloat(((humidity_temp+humid_now)/(counter+1)).toFixed(2));
			console.log('');
			console.log('Time: ' + counter*10 + ' seconds');
			counter++;
			console.log('Present Temperature: ' + temp_now.toFixed(2) + '°F, ' +'Present Humidity: ' + humid_now.toFixed(2) + '%');
			console.log('Maximum Temperature: ' + temp_max.toFixed(2) + '°F, ' +'Maximum Humidity: ' + humid_max.toFixed(2) + '%');
			console.log('Minimum Temperature: ' + temp_min.toFixed(2) + '°F, ' +'Minimum Humidity: ' + humid_min.toFixed(2) + '%');
			console.log('Average Temperature: ' + temp_avg.toFixed(2) + '°F, ' +'Average Humidity: ' + humid_avg.toFixed(2) + '%');
			setTimeout(ht_read, 10000);
	});
}

ht_read();

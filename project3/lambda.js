//Initializations
var AWS = require('aws-sdk');
AWS.config.update({region: 'REGION'});
var sqs = new AWS.SQS();
var avg_temp = 0.00;
var avg_humid = 0.00;
var max_temp = 0.00;
var max_humid = 0.00;
var min_temp = 100.00;
var min_humid = 100.00;
var count_temp = 1.0;
var count_humid = 1.0;

//Handler for event detection
exports.handler = (event, context, callback) => {
    var eventText = JSON.stringify(event, null, 2);
    console.log("Received event:", eventText);
    // Taking values received from the IoT topic
    var curr_temp = parseFloat(event.Temperature);
    var curr_humid = parseFloat(event.Humidity);
    //Finding max,min,avg values
    if(curr_temp>0)
    {
        avg_temp=((avg_temp*count_temp)+curr_temp)/(count_temp+1);
        count_temp+=1;
        max_temp = Math.max(max_temp, curr_temp);
        min_temp = Math.min(min_temp, curr_temp);
        avg_temp = avg_temp.toFixed(2);
        max_temp = max_temp.toFixed(2);
        min_temp = min_temp.toFixed(2);
    } 
    if(curr_humid>0)
    {
        avg_humid=((avg_humid*count_humid)+curr_humid)/(count_humid+1);
        count_humid+=1;
        max_humid = Math.max(max_humid, curr_humid);
        min_humid = Math.min(min_humid, curr_humid);
        avg_humid = avg_humid.toFixed(2);
        max_humid = max_humid.toFixed(2);
        min_humid = min_humid.toFixed(2);
    } 
    
    //Message to be written JSON format
    var params = {
     DelaySeconds: 0,
     MessageBody: "{ \"curr_temp\": " + curr_temp +", " + " \"avg_temp\": " + avg_temp + "," + "\"max_temp\": " + max_temp + "," + "\"min_temp\": " + min_temp + "," +"\"curr_humid\": " + curr_humid + "," + "\"avg_humid\": " + avg_humid + "," + "\"max_humid\": " + max_humid + "," + "\"min_humid\": " + min_humid + "}",
     QueueUrl: "https://sqs.us-east-1.amazonaws.com/275213791663/temperature_humidity_queue"
    };

    //Message sending
    sqs.sendMessage(params, function(err,data){
    if(err) {
      console.log('error:',"Fail Send Message" + err);
    }else{
      console.log('data:',data.MessageId);
    }
});
    //Value logging for cloudwatch
    console.log(max_temp, min_temp, max_humid, min_humid, avg_temp, avg_humid, count_temp, count_humid);
    callback(null, curr_humid);
};


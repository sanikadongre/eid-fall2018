// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};

$(document).ready(function () {
  var ws;
  var temp;
  var avg_temp;
  var maxtemp; 
  var mintemp;
  var celsiusunit; 
  var faranunit;
 ws = new WebSocket("ws://10.0.0.241:8888/ws")

//Error handling for websockets
  ws.onerror = function(error){
    alert("Cannot connect to server. Make sure server is online")
  }
 ws.onclose = function(evt) {
      alert("Retry Refreshing the Webpage!");
    }
//handling Messages from tornado server
  ws.onmessage = function(evt) {
  // log("Message Received: " + evt.data)
  //alert("message received: " + evt.data)
    var str_arry = evt.data.split(" ")

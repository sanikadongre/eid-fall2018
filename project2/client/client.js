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
 
window.onload = function(){

var clock = document.getElementById('clock');


function mainClock(){

   var time = new Date();
   
   var h = time.getHours().toString();
   var m = time.getMinutes().toString();
   var s = time.getSeconds().toString();



   if (h.length < 2){

     h = '0' + h;

   }


if (m.length < 2){

     m = '0' + m;

   }


   if (s.length < 2){

     s = '0' + s;

   }




var clockstring = h + ':' + m + ':' + s;


clock.textContent = clockstring; 
}

setInterval(mainClock, 1000);

}
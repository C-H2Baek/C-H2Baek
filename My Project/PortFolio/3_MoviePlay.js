var i=0;
var txt="Your browser does not support the video tag.";
var speed=50;
function type(){
  document.getElementById("type").innerHTML
    +=txt.charAt(i);
  i++;
  setTimeout(type,speed);
}
type(); 
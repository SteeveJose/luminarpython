var student=prompt("enter the name of te student:");
var m1=Number(prompt("mark for chemistry:"));
var m2=Number(prompt("mark of physics:"));
var m3=Number(prompt("mark of Maths:"));
var to_mark=Number(m1+m2+m3);
if(to_mark<130){
    alert(student+"failed")}
else if((130<to_mark)&&(to_mark<135)){
    alert(student+"got grade:B")}
else if((135<to_mark)&&(to_mark<140)){
    alert(student+"got grade:B+")}
else if((140<to_mark)&&(to_mark<145)){
    alert(student+"got grade:A")}
else{
    alert(student+"got grade:A+")}
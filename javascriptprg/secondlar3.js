var num1=prompt("enter the first number:");
var num2=prompt("enter the second number:");
var num3=prompt("enter the third number:");
if (num1>num2 && num1>num3){
    if(num2>num3){
        alert(num2+"is the second largest number")}
    else{
        alert(num3+"is the second largest number")}}
else if (num2>num1 && num2>num3){
    if(num1>num3){
        alert(num2+"is the second largest number")}
    else{
        alert(num3+ "is the second largest number")}}
else if (num3>num1 && num3>num2){
    if(num1>num2){
        alert(num1+ "is the second largest number")}
    else{
        alert(num2+ "is the second largest number")}}
else{
     alert("nothing");}
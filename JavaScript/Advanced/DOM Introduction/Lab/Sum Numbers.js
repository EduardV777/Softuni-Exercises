function calc() {
  var but=document.getElementsByTagName('input');
  var f1=document.getElementById('num1');
  var f2=document.getElementById('num2');
  var f3=document.getElementById('sum');
  var num1=Number(f1.value);
  var num2=Number(f2.value);
  f3.value=num1+num2;
}

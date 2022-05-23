function FindGCD(num1, num2){
  var div=1, GCD=0;
  while(true){
    if(div>num1 && div>num2){
      break;
    }
    if(num1%div==0 && num2%div==0){
      GCD=div;
    }
    div++;
  }
  console.log(GCD);
}

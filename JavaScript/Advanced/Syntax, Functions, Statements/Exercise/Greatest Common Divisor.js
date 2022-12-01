function FindGCD(num1, num2){
  let gcd = 0, div = 1;

  while(true){
      if(num1 % div == 0 && num2 % div == 0){
          gcd = div;
      }

      if(div > num1 && div > num2){
          break;
      }

      div++;
  }

  console.log(gcd);
}

FindGCD(15, 5);
FindGCD(2154, 458);
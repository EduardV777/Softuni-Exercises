function checkIfSameDigits(number){
  let strNumber = String(number);
  let sameDigits = true;
  let sumOfDigits = 0;

  for(let k = 0; k < strNumber.length; k++){
      if(strNumber[k] != strNumber[0]){
          sameDigits = false;
      }

      sumOfDigits += Number(strNumber[k]);
  }

  console.log(sameDigits);
  console.log(sumOfDigits);
}


checkIfSameDigits(2222222);
checkIfSameDigits(1234);
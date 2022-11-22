function findLargest(num1, num2, num3){
  let largestNumber;
  if(num1 > num2){
      largestNumber = num1;
  }else {
      largestNumber = num2;
  }

  if(largestNumber < num3){
      largestNumber = num3;
  }

  console.log(`The largest number is ${largestNumber}.`);
}

findLargest(5, -3, 16);
findLargest(-3, -5, -22.5);
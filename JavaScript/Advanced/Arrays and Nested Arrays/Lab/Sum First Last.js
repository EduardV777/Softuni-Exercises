function sumFirstLastElement(arr){
  let sum = Number(arr[0]) + Number(arr[arr.length - 1]);
  console.log(sum);
}

sumFirstLastElement(['20', '30', '40']);
sumFirstLastElement(['5', '10']);
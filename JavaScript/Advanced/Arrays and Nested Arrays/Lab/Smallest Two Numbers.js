function findTwoSmallest(arr){
  let output = "", smallestNumber;
  
  for(let k = 0; k < arr.length; k++){
      for(let j = 0; j < arr.length - 1; j++){
          if(arr[j] > arr[j+1]){
              let curr = arr[j+1];
              arr[j+1] = arr[j];
              arr[j] = curr;
          }
      }
  }

  output += arr[0] + " " + arr[1];

  console.log(output);
}

findTwoSmallest([30, 15, 50, 5]);
findTwoSmallest([3, 0, 10, 4, 7, 3]);
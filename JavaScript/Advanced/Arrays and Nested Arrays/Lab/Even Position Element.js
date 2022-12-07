function findEvenElements(arr){
  let evenElements = "";

  for(let k = 0; k < arr.length; k++){
      if(k % 2 == 0){
          evenElements += arr[k] + " ";
      }
  }

  console.log(evenElements);
}

findEvenElements(['20', '30', '40', '50', '60']);
findEvenElements(['5', '10']);
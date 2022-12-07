function processArray(arr) {
  let newArray = new Array();

  for(let k = 0; k < arr.length; k++){
      if(arr[k] < 0){
          newArray.unshift(arr[k]);
      }else {
          newArray.push(arr[k]);
      }
  }

  for(let k = 0; k < newArray.length; k++){
      console.log(newArray[k]);
  }
}


processArray([7, -2, 8, 9]);
processArray([3, -2, 0, -1]);
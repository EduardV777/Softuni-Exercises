function returnHalf(arr){
    
  let sortArray = function SortArray(a,b){
          if(a > b){
              return 1;
          }else {
              return -1;
          }
          return 0;
      }
  
  arr.sort(sortArray);

  let halfArr = new Array();

  if(arr.length % 2 == 0){
      let k = arr.length / 2;

      for(;k < arr.length; k++){
          halfArr.push(arr[k]);
      }
  }else {
      let k = Math.floor(arr.length / 2);
      halfArr = arr.slice(0, k);

      if(halfArr.length < arr.slice(k, arr.length).length){
          halfArr = arr.slice(k, arr.length);
      }
  }

  return halfArr;

}

console.log(returnHalf([4, 7, 2, 5]));
console.log(returnHalf([3, 19, 14, 7, 2, 19, 6]));
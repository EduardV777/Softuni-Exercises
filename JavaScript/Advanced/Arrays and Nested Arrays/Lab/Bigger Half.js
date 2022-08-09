function BiggerHalf(array){
  array = array.sort((a,b) => a-b);
  console.log(array);
  array2 = [];
  if(array.length % 2 == 0){
    array2 = array.slice(array.length / 2);
  }else {
    if(array.length / 2 >= array.length - array.length / 2){
      array2 = array.slice(array.length / 2);
    }else {
      array2 = array.slice(0, array.length / 2);
    }
  }
  console.log(array2);
}

console.log(BiggerHalf([4,7,2,5]));
console.log(BiggerHalf([3, 19, 14, 7, 2, 19, 6]));
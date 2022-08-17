<<<<<<< HEAD
function ReturnHalf(arr){
  for(var i=0;i<arr.length-1;i++){
    for(var j=0;j<arr.length-1;j++){
      if(arr[j]>arr[j+1]){
        var temp=arr[j+1];
        arr[j+1]=arr[j];
        arr[j]=temp;
      }
    }
  }
  length=arr.length;
  var half1=arr.slice(0,Math.floor(length/2));
  var half2=arr.slice(Math.floor(length/2));
  if(length%2!=0){
    if(half1.length>half2.length){
      console.log(half1);
    }else {
      console.log(half2);
    }
  }
  else {
    console.log(half2);
  }
}
=======
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
>>>>>>> a796fc383b6d7a1e2b40c52280ee5f85b44360db

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

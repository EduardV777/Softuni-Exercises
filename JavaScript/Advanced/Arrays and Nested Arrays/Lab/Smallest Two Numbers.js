function FindTwoSmallestElements(arr){
  //sorting
  for(var i=0;i<arr.length-1;i++){
    for(var j=0;j<arr.length-1;j++){
      if(arr[j]>arr[j+1]){
        var temp=arr[j+1];
        arr[j+1]=arr[j];
        arr[j]=temp;
      }
    }
  }
  //sorting ends
  output=arr[0]+" "+arr[1];
  console.log(output);
}

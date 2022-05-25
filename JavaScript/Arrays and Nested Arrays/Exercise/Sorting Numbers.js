function SortNumbers(arr){
  var sortedArray=[], k=1;
  for(var i=0;i<arr.length-1;i++){
    for(var j=0;j<arr.length-1;j++){
      if(arr[j]>arr[j+1]){
        temp=arr[j+1];
        arr[j+1]=arr[j];
        arr[j]=temp;
      }
    }
  }

  while(arr.length!=0){
    if(k==1){
      sortedArray.push(arr[0]);
      arr.shift();
      k++;
    }else if(k==2){
      sortedArray.push(arr[arr.length-1]);
      arr.pop();
      k--;
    }
  }
  return sortedArray
}
/*
the first element is the smallest one,
the second is the biggest one,
the third is the second smallest one,
the fourth is the second biggest one, and so on.
*/

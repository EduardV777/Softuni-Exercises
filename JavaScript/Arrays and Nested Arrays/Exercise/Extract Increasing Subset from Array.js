function Extract(arr){

  function SortAndClear(arrayToSort){
    for(var i=0;i<arrayToSort.length-1;i++){
      for(var j=0;j<arrayToSort.length-1;j++){
        if(arrayToSort[j]>arrayToSort[j+1]){
          var temp=arrayToSort[j+1];
          arrayToSort[j+1]=arrayToSort[j];
          arrayToSort[j]=temp;
        }
      }
    }
    while(arrayToSort.indexOf(-999)!=-1){
      arrayToSort.shift();
    }
  }

  currentNumber=0;
  subSet=arr.map(function(x){ if(currentNumber<x){ currentNumber=x; return x } else { return -999 } });
  SortAndClear(subSet);
  while(subSet.indexOf(false)!=-1){
    subSet.pop(subSet.indexOf(false));
  }
  //console.log(subSet);
  return subSet;
}

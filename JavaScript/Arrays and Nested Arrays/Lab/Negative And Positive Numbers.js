function ProcessArray(arr){

  for(var i in arr){
    if(Number(arr[i])<0){
      arr[i].unshift();
    }
  }

}

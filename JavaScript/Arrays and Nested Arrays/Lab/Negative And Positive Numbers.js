function GetNewArray(arr){
  output="";
  newArray=Array();
  for(var k=0;k<arr.length;k++){
    if(arr[k]<0){
      newArray.unshift(arr[k]);
    }else {
      newArray.push(arr[k]);
    }
  }

  for(var i in newArray){
    output+=newArray[i]+"\n";
  }
  console.log(output);
}

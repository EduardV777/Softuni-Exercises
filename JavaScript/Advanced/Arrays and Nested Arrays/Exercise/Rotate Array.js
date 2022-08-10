function RotateArray(arr, rotations){
  output="";
  for(var i=0;i<rotations;i++){
    var elem=arr.pop();
    arr.unshift(elem);
  }

  for(var e in arr){
    output+=arr[e]+" ";
  }
  console.log(output);
}

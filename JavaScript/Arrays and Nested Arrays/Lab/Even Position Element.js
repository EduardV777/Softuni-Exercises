function FindEvenPosElements(arr){
  output="";
  for(var k=0;k<arr.length;k++){
    if(k%2==0){
      output+=arr[k]+" ";
    }
  }
  console.log(output);
}

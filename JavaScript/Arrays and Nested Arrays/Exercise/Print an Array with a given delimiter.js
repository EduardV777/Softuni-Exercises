function ShowArray(stringArr, delimit){
  output=""
  for(var i=0;i<stringArr.length;i++){
    output+=stringArr[i];
    if(i!=stringArr.length-1){
      output+=delimit;
    }
  }
  console.log(output);
}

function ShowElements(stringArr, n){
  outputArr=[];
  for(var i=0;i<stringArr.length;i+=n){
    outputArr.push(stringArr[i]);
  }
  console.log(outputArr.join("\n"));
}

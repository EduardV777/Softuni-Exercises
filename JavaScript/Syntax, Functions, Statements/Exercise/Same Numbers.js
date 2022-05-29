function SameOrNot(number){
  var same=true;
  var numStr=String(number);
  var sum=Number(numStr[0]);
  for(var k=1;k<numStr.length;k++){
    sum+=Number(numStr[k]);
    if(numStr[k]!=numStr[k-1]){
      same=false;
    }
  }

  console.log(same);
  console.log(sum);
}

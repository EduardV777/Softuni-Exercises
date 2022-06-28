function Sequence(n,k){
  var sequence=[], output="[";
  for(var j=0;j<n;j++){
    var back=k, sum=0;
    if(j==0){
      sequence.push(1);
    }else {
      while(back!=0){
        if(j-back>=0){
          sum+=sequence[j-back];
        }
        back--;
      }
      sequence.push(sum);
    }
  }
  console.log("["+sequence.join(', ')+"]");
}

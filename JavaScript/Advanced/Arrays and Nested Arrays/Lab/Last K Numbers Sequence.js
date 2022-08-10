<<<<<<< HEAD
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
=======






// function Sequence(n,k){
//   var sequence=[], output="[";
//   for(var j=0;j<n;j++){
//     var back=k, sum=0;
//     if(j==0){
//       sequence.push(1);
//     }else {
//       while(back!=0){
//         if(j-back>=0){
//           sum+=sequence[j-back];
//         }
//         back--;
//       }
//       sequence.push(sum);
//     }
//   }
//   console.log("["+sequence.join(', ')+"]");
// }
>>>>>>> a796fc383b6d7a1e2b40c52280ee5f85b44360db

function Sum(arr){
  var sum=0;
  for(var k=0;k<arr.length;k++){
    sum+=arr[k];
  }
  console.log(sum);
}

function SumInverse(arr){
  var sum=0;
  for(var k=0;k<arr.length;k++){
    sum+=1/arr[k];
  }
  console.log(sum);
}

function Concat(arr){
  var con="";
  for(var k in arr){
    con+=arr[k].toString();
  }
  console.log(con);
}
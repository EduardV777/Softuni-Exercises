function SortedNames(arr){
  var k=1, output="";
  arr.sort();
  for(var e in arr){
    output+=k+"."+arr[e]+"\n";
    k++;
  }
  console.log(output);
}

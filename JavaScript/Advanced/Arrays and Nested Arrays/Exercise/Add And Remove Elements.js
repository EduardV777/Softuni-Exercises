function AddRemove(commandArr){
  var num=1, numArray=[], output="";
  for(var i=0;i<commandArr.length;i++, num++){
    if(commandArr[i]=='add'){
      numArray.push(num);
    }else if(commandArr[i]=='remove'){
      numArray.pop();
    }
  }
  if(numArray.length==0){
    output="Empty"
  }else {
    for(var e in numArray){
      output+=numArray[e]+"\n";
    }
  }
  console.log(output);
}

function ShowStarsSquare(size){
  if(typeof(size)=="undefined"){
    size=5;
  }
  var output=""
  for(var k=1;k<=size;k++){
    var row="";
    for(var j=1;j<=size;j++){
      row+="* ";
    }
    output+=row+"\n";
  }
  console.log(output);
}

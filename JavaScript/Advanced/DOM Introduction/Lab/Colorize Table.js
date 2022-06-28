function colorizeRows(){
  var rows=document.querySelectorAll("table tr");
  var ind=0;
  for(var r of rows){
    ind++;
    if(ind%2==0){
      r.style.background='teal';
    }
  }
}

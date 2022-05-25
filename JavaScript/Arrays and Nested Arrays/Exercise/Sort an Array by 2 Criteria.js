function sortStringArray(stringArr){
  var k=0, output="";
  while(k<=1){
    for(var i=0;i<stringArr.length-1;i++){
      for(var j=0;j<stringArr.length-1;j++){
          if(k==0){
            if(stringArr[j].length>stringArr[j+1].length){
              var temp=stringArr[j+1];
              stringArr[j+1]=stringArr[j];
              stringArr[j]=temp;
            }
          }else {
            val1=0; val2=0;
            for(var e in stringArr[j]){
              val1+=stringArr[j][e].charCodeAt(0);
            }
            for(var e in stringArr[j+1]){
              val2+=stringArr[j+1][e].charCodeAt(0);
            }
            if(val1>val2){
              var temp=stringArr[j+1];
              stringArr[j+1]=stringArr[j];
              stringArr[j]=temp;
            }
          }

        }
      }
      k++;
  }
  for(var e in stringArr){
    output+=stringArr[e]+"\n"
  }
  console.log(output);
}


/*
Sort strings by a length in ascending order as primary criteria,
Sort by alphabetical value in ascending order as second criteria.
The comparison should be case-insensitive.
*/

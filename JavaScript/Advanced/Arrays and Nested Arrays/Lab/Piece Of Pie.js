function GetFlavorArray(flavorArr, targetFlavor1, targetFlavor2){
  var newArr=[], output="";
  for(var i=0;i<flavorArr.length;i++){
    if(flavorArr[i]==targetFlavor1){
      var k=i;
      while(k<flavorArr.length){
        newArr.push(flavorArr[k]);
        if(flavorArr[k]==targetFlavor2){
          break;
        }
        k++;
      }
      break;
    }
  }
  console.log(newArr);
}

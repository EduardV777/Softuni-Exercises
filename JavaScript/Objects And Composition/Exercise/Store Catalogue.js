function CreateCatalogue(stringsArray){
  //"{productName} : {productPrice}"
  var catalogue = {}, letter="";

  for(var k = 0; k < stringsArray.length; k++){
    stringsArray[k] = stringsArray[k].split(" : ");
    catalogue[stringsArray[k][0]] = Number(stringsArray[k][1]);
  }

  objKeys=Object.keys(catalogue);
  objKeys.sort();
  catalogueSorted = {}

  for(var k = 0; k < objKeys.length; k++){
    catalogueSorted[objKeys[k]] = catalogue[objKeys[k]];
  }

  for(var prod in catalogueSorted){
    if(letter != prod[0]){
      letter = prod[0]
      console.log(letter);
    }
    console.log("  "+prod+": "+catalogueSorted[prod])

  }

}


CreateCatalogue(['Appricot : 20.4', 'Fridge : 1500', 'TV : 1499', 'Deodorant : 10', 'Boiler : 300', 'Apple : 1.25', 'Anti-Bug Spray : 15', 'T-Shirt : 10']);

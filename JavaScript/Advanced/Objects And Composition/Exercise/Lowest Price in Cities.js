function FindLowestPrice(stringsArray) {
  //{townName} | {productName} | {productPrice}
  products = {};

  for(var k = 0; k < stringsArray.length; k++){
    stringsArray[k] = stringsArray[k].split(" | ");

    if(stringsArray[k][1] in products){
      products[stringsArray[k][1]].push([stringsArray[k][0], Number(stringsArray[k][2])]);
    }else {
      products[stringsArray[k][1]] = [[stringsArray[k][0], Number(stringsArray[k][2])]];
    }

  }

  for(var prod in products){
    var cityName = "", price = 2147000000;

    for(var k = 0; k < products[prod].length; k++){
        if(products[prod][k][1] < price){
          price = products[prod][k][1];
          cityName = products[prod][k][0];
        }
    }

    console.log(prod+" -> "+price+" ("+cityName+")");
  }

}

/*
FindLowestPrice(['Sample Town | Sample Product | 1000',

'Sample Town | Orange | 2',

'Sample Town | Peach | 1',

'Sofia | Orange | 3',

'Sofia | Peach | 2',

'New York | Sample Product | 1000.1',

'New York | Burger | 10']);
*/

FindLowestPrice(['Sofia City | Audi | 100000',
'Sofia City | BMW | 100000',
'Sofia City | Mitsubishi | 10000',
'Sofia City | Mercedes | 10000',
'Sofia City | NoOffenseToCarLovers | 0',
'Mexico City | Audi | 1000',
'Mexico City | BMW | 99999'])

/*

Sample Product -> 1000 (Sample Town)
Orange -> 2 (Sample Town)
Peach -> 1 (Sample Town)
Burger -> 10 (New York)


*/

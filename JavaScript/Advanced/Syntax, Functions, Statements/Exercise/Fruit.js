function returnTotal(fruitType, weightGr, pricePerKg){
  let weightKg = weightGr / 1000
  let total = weightKg * pricePerKg;
  console.log(`I need $${total.toFixed(2)} to buy ${weightKg.toFixed(2)} kilograms ${fruitType}.`);
}

returnTotal('orange', 2500, 1.80);
returnTotal('apple', 1563, 2.35);
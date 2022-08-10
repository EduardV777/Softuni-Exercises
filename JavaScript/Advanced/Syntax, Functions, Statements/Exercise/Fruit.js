function CalculatePrice(typeOfFruit, weightGr, PricePerKg){
  PricePerKg/=1000;
  var total=PricePerKg*weightGr;
  var weightKg=weightGr/1000
  console.log("I need $"+total.toFixed(2)+" to buy "+weightKg.toFixed(2)+" kilograms "+typeOfFruit+".");
}

function cityTaxes(cityName, population, treasury){
  cityData={'name':cityName, 'population': population, 'treasury':treasury, 'taxRate': 10,
            'collectTaxes':function() { this.treasury=Math.floor(eval(this.population*this.taxRate));},
            'applyGrowth':function(pct){ this.population=Math.floor(eval(this.population*(pct/100)));},
            'applyRecession':function(pct){this.treasury=Math.floor(eval(this.treasury-(this.treasury*(pct/100))));} };

  return cityData;
}

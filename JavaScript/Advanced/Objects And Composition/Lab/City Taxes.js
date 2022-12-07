function cityTaxes(cityName, population, treasury){
  let obj = {name: cityName, population: population, treasury: treasury, taxRate: 10};

  let collectTaxes = function () {
      this.treasury += this.population * this.taxRate;
  }

  let applyGrowth = function(pct) {
      this.population += Math.floor(this.population * (pct / 100));
  }

  let applyRecession = function(pct) {
      this.treasury -= Math.floor(this.treasury * (pct / 100));
  }

  obj.collectTaxes = collectTaxes;
  obj.applyGrowth = applyGrowth;
  obj.applyRecession = applyRecession;

  return obj;
}




const city = cityTaxes('Tortuga', 7000, 15000);
console.log(city);



const city2 = cityTaxes('Tortuga', 7000, 15000);
city2.collectTaxes();
console.log(city2.treasury);
city2.applyGrowth(5);
console.log(city2.population);
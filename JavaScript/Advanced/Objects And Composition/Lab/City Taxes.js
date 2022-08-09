function cityTaxes(name, population, treasury){
  let obj = {name: name, population: population, treasury: treasury, taxRate: 10,
    collectTaxes: function() {
      this.treasury += Math.floor(this.population * this.taxRate);
    },
    applyGrowth(pct){
      this.population += Math.floor(this.population * (pct / 100));
    },
    applyRecession(pct){
      this.treasury -= Math.floor(this.treasury * (pct / 100));
    }
  };

  return obj;

}

// const city = 
//   cityTaxes('Tortuga',
//   7000,
//   15000);
// console.log(city);

const city =
  cityTaxes('Tortuga',
  7000,
  15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
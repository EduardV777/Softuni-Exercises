function findCircleArea(r) {

  if(typeof(r) != 'number'){
      console.log(`We can not calculate the circle area, because we receive a ${typeof(r)}.`);
  }else {
      let area = Math.pow(r, 2) * Math.PI;
      console.log(area.toFixed(2));
  }
}

findCircleArea(5);
findCircleArea('name');
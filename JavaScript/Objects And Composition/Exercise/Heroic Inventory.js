function HeroesRegister(dataArray) {

    register = [];
    for(var k = 0; k < dataArray.length; k++){
      dataArray[k] = dataArray[k].split(" / ");
      register.push({});
      register[k]['name'] = dataArray[k][0];
      dataArray[k].shift();
      register[k]['level'] = Number(dataArray[k][0]);
      dataArray[k].shift();
      register[k]['items'] = [];
      dataArray[k][0] = dataArray[k][0].split(", ");

      if(dataArray[k][0].length != 0){
        for(var j = 0; j < dataArray[k].length; j++){

          for(var i = 0; i < dataArray[k][0].length; i++){
              register[k]['items'].push(dataArray[k][0][i]);
          }

        }
      }

    }

    console.log(JSON.stringify(register))
}

HeroesRegister(['Isacc / 25 / Apple, GravityGun',
'Derek / 12 / BarrelVest, DestructionSword',
'Hes / 1 / Desolator, Sentinel, Antara']);

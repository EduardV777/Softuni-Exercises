function ProcessOrder(orderObj){
    resultingOrder = {model: orderObj.model};

    if(orderObj.power <= 90 || Math.abs(orderObj.power-90) < Math.abs(orderObj.power-120)){
      //Small engine
      powerEngine = 90;
      volume = 1800;
    }else if(orderObj.power <= 120 || Math.abs(orderObj.power-120) < Math.abs(orderObj.power-200)){
      //Normal engine
      powerEngine = 120;
      volume = 2400;
    }else if(orderObj.power == 200){
      //Monster engine
      powerEngine = 200;
      volume = 3500;
    }
    resultingOrder['engine'] = {power: powerEngine, volume: volume};
    wheelSize = orderObj.wheelsize;

    carColor = orderObj.color;
    resultingOrder['carriage'] = {type: orderObj.carriage, color: carColor};

    while(true){
      if(wheelSize % 2 == 0){
        wheelSize -= 0.5;
        wheelSize = Math.floor(wheelSize);
      } else {
        break;
      }
    }
    resultingOrder['wheels'] = [wheelSize, wheelSize, wheelSize, wheelSize];

    return resultingOrder;
}


ProcessOrder({ model: 'Opel Vectra',
power: 110,
color: 'grey',
carriage: 'coupe',
wheelsize: 17 });

/*
Engines:
Small engine: { power: 90, volume: 1800 }
Normal engine: { power: 120, volume: 2400 }
Monster engine: { power: 200, volume: 3500 }

Carriages:
Hatchback: { type: 'hatchback', color: <as required> }
Coupe: { type: 'coupe', color: <as required> }

*/




/*
Order

{ model: 'VW Golf II',
power: 90,
color: 'blue',
carriage: 'hatchback',
wheelsize: 14 }

*/

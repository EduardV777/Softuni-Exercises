function CreateObject(valuesArray){
    var foodData = Object.create(Object.prototype), currentFood = "";

    for(var k=0;k<valuesArray.length;k++){
        if(k%2==0){
          currentFood=valuesArray[k];
          foodData[currentFood] = 0;
        }else {
          foodData[currentFood] = Number(valuesArray[k]);
        }
    }

    return console.log(foodData);
}


CreateObject(['Yoghurt', '48', 'Rise', '138', 'Apple', '52']);

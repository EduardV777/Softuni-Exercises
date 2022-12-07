function registry(stringsArr){
  let regObj = {};

  for(let k = 0; k < stringsArr.length; k++){
      let keyVal = stringsArr[k].split(" <-> ")

      if(keyVal[0] in regObj){
          regObj[keyVal[0]] += Number(keyVal[1]);
      }else{
          regObj[keyVal[0]] = Number(keyVal[1]);
      }
  }

  for(let city in regObj){
      console.log(`${city} : ${regObj[city]}`);
  }
}

registry(['Sofia <-> 1200000', 'Montana <-> 20000', 'New York <-> 10000000', 'Washington <-> 2345000', 'Las Vegas <-> 1000000']);
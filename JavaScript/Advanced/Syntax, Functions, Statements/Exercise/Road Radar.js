function IsWithinLimit(speed, area){
<<<<<<< HEAD
  if(area=="city"){
    speedLimit=50;
  }
  else if(area=="motorway"){
    speedLimit=130;
  }
  else if(area=="interstate"){
    speedLimit=90;
  }
  else if(area=="residential"){
    speedLimit=20;
  }

  if(speed<=speedLimit){
    console.log("Driving "+speed+" km/h in a "+speedLimit+" zone")
  }else {
    diff=speed-speedLimit;
    if(diff<=20){
      status="speeding";
    }else if(diff<=40){
      status="excessive speeding";
    }else{
      status="reckless driving";
    }
    console.log("The speed is "+diff+" km/h faster than the allowed speed of "+speedLimit+" - "+status);
  }
}
=======
  let speedLimit, speedStatus;
  function CheckSpeed(){
    switch(area){
      case "motorway":
        speedLimit = 130;
        if(speed > speedLimit){
          return true;
        }else {
          return false;
        }
      case "interstate":
        speedLimit = 90;
        if(speed > speedLimit){
          return true;
        }else {
          return false;
        }
      case "city":
        speedLimit = 50;
        if(speed > speedLimit){
          return true;
        }else {
          return false;
        }
      case "residential":
        speedLimit = 20;
        if(speed > speedLimit){
          return true;
        }else {
          return false;
        }
    }
  }

  if(CheckSpeed()){
    let speedingAmount = speed - speedLimit;
    if(speedingAmount <= 20){
        speedStatus = "speeding";
    } else if (speedingAmount <= 40){
      speedStatus = "excessive speeding";
    } else {
      speedStatus = "reckless driving";
    }
    console.log(`The speed is ${speedingAmount} km/h faster than the allowed speed of ${speedLimit} - ${speedStatus}`);
  }else {
    console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
  }
}

IsWithinLimit(40, 'city');
IsWithinLimit(21, 'residential');
IsWithinLimit(120, 'interstate');
IsWithinLimit(200, 'motorway');
>>>>>>> a796fc383b6d7a1e2b40c52280ee5f85b44360db

function IsWithinLimit(speed, area){
  let withinLimit = true;
  let speedDiff = 0, speedingStatus = "", speedLimit = 0;

  switch(area){
      case "motorway":
          speedLimit = 130;
          if(speed > 130){
              withinLimit = false;
              speedDiff = speed - 130;
          }
          break;
      case "interstate":
          speedLimit = 90;
          if(speed > 90){
              withinLimit = false;
              speedDiff = speed - 90;
          }
          break;
      case "city":
          speedLimit = 50;
          if(speed > 50){
              withinLimit = false;
              speedDiff = speed - 50;
          }
          break;
      case "residential":
          speedLimit = 20;
          if(speed > 20){
              withinLimit = false;
              speedDiff = speed - 20;
          }
          break;
  }

  if(withinLimit){
      console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
  }else {
      if(speedDiff <= 20){
          speedingStatus = "speeding"
      }else if(speedDiff <= 40){
          speedingStatus = "excessive speeding";
      }else{
          speedingStatus = "reckless driving";
      }

      console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${speedLimit} - ${speedingStatus}`);
  }
}


IsWithinLimit(40, 'city');
IsWithinLimit(21, 'residential');
IsWithinLimit(120, 'interstate');
IsWithinLimit(200, 'motorway');
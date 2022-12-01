function calculateTime(numberOfSteps, footprintLengthM, speedKMH){
    let totalTimeS = 0, hours, minutes, seconds;

    let distancePassed = numberOfSteps * footprintLengthM;
    let speedS = speedKMH / 3.6;
    totalTimeS += (distancePassed / speedS) + ((Math.floor(distancePassed / 500)) * 60);

    hours = Math.floor(totalTimeS / 3600);
    minutes = Math.floor(totalTimeS / 60);
    seconds = Math.round(totalTimeS - (hours * 3600) - (minutes * 60));

    if(hours < 10){
        hours = String("0" + hours);
    }
    if(minutes < 10){
        minutes = String("0" + minutes);
    }
    if(seconds < 10){
        seconds = String("0" + seconds);
    }
    
    console.log(`${hours}:${minutes}:${seconds}`)
}


calculateTime(4000, 0.60, 5);
calculateTime(2564, 0.70, 5.5);
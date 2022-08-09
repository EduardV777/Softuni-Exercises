function TimeToWalk(numberOfSteps, footPrintM, speed){
    let time, timeString = "", k = 0;
    let distancePassed = numberOfSteps * footPrintM;
    let speedPerSec = speed / 3.6;
    time = distancePassed / speedPerSec + ( 60 * (Math.floor(distancePassed / 500)));

    let hours = Math.floor(time / 60 / 60);
    let minutes = Math.floor(time / 60);
    let seconds = Math.round(time - hours * (60 * 2) - minutes * 60);

    function processTimeString(arg, k){
        if(arg < 1){
            timeString += "00";
        }else if(arg < 10){
            timeString += "0" + arg;
        }else {
            timeString += arg;
        }

        if(k != 2){
            timeString += ":";
        }
    }

    while(k < 3){
        if(k == 0){
            processTimeString(hours, k);
        }else if(k == 1){
            processTimeString(minutes, k);
        }else if(k == 2){
            processTimeString(seconds, k);
        }
        k++;
    }

    console.log(timeString);
}

TimeToWalk(4000, 0.60, 5);
TimeToWalk(2564, 0.70, 5.5);
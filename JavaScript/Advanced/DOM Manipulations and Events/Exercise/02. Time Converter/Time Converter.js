function attachEventsListeners() {
    let daysField = document.getElementById('days');
    let hoursField = document.getElementById('hours');
    let minutesField = document.getElementById('minutes');
    let secondsField = document.getElementById('seconds');
    let buttons = document.querySelectorAll('input[type="button"]');

    for(var k = 0; k < buttons.length; k++){
        buttons[k].addEventListener('click', Convert);
    }


    function Convert(){
        let id = this.id;
        
        if(id == "daysBtn"){
            let daysCount = Number(daysField.value);
            hoursField.value = daysCount * 24;
            minutesField.value = daysCount * 1440;
            secondsField.value = daysCount * 86400;

        }else if(id == "hoursBtn"){
            let hoursCount = Number(hoursField.value);
            daysField.value = hoursCount / 24;
            minutesField.value = hoursCount * 60;
            secondsField.value = hoursCount * 3600;

        }else if(id == "minutesBtn"){
            let minutesCount = Number(minutesField.value);
            daysField.value = minutesCount / 1440;
            hoursField.value = minutesCount / 60;
            secondsField.value = minutesCount * 60;

        }else if(id == "secondsBtn"){
            let secondsCount = Number(secondsField.value);
            daysField.value = secondsCount / 86400;
            hoursField.value = secondsCount / 3600;
            minutesField.value = secondsCount / 60;
        }
    }

}
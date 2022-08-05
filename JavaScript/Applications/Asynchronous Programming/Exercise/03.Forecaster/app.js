let getWeatherButton = document.querySelector("input#submit");
let forecastSection = document.querySelector("div#forecast");
let currentSection = document.querySelector("div#current");
let upcomingSection = document.querySelector("div#upcoming");

async function attachEvents() {
    let forecast = "", forecast3Days = "";

    let location = document.querySelector("input#location").value;

    let locationsArray = await fetch('http://localhost:3030/jsonstore/forecaster/locations')
        .then((response) => response.json())
        .then((obj) => {return obj});
    
    let match = false;

    for(var k = 0; k < locationsArray.length; k++){

        if(locationsArray[k].name == location){
            let currentForecast = "", upcomingForecast = "";
            match = true;
            let code = locationsArray[k].code
            forecast = await fetch(`http://localhost:3030/jsonstore/forecaster/today/${code}`)
                            .then((resp) => resp.json())
                            .then((res) => {return res});
            
            if (forecast.condition == "Sunny"){
                currentForecast += "&#x2600;";
            }else if (forecast.condition == "Rain"){
                currentForecast += "&#x2614;";
            }else if (forecast.condition == "Overcast"){
                currentForecast += "&#x2601;";
            }else if (forecast.condition == "Partly sunny"){
                currentForecast += "&#x26C5;"
            }

            currentForecast += `${forecast.name}\n${forecast.forecast.low}&#176;/${forecast.forecast.high}&#176;\n${forecast.forecast.condition}`;

            console.log(forecast);
            console.log(currentForecast);
            
            forecast3Days = await fetch(`http://localhost:3030/jsonstore/forecaster/upcoming/${code}`)
                                    .then((resp) => resp.json())
                                    .then((res) => {return res});
            console.log(forecast3Days);

            for(var j = 0; j < forecast3Days.forecast.length; j++){
                if (forecast3Days.forecast[j].condition == "Sunny"){
                    upcomingForecast += "&#x2600;\n";
                }else if (forecast3Days.forecast[j].condition == "Rain"){
                    upcomingForecast += "&#x2614;\n";
                }else if (forecast3Days.forecast[j].condition == "Overcast"){
                    upcomingForecast += "&#x2601;\n";
                }else if (forecast3Days.forecast[j].condition == "Partly sunny"){
                    upcomingForecast += "&#x26C5;\n"
                }

                upcomingForecast += `${forecast3Days.forecast[j].low}&#176;/${forecast3Days.forecast[j].high}&#176;\n${forecast3Days.forecast[j].condition}  `;
            }
            p1 = document.createElement("p");
            p2 = document.createElement("p");

            p1.innerHTML = currentForecast;
            p2.innerHTML = upcomingForecast;

            forecastSection.style.display = "block";
            currentSection.appendChild(p1);
            upcomingSection.appendChild(p2);
            break;
        }
    }
    if(match == false){
        forecastSection.textContent = "Error"; forecastSection.style.display = "block";
    }
}


getWeatherButton.addEventListener("click", attachEvents);
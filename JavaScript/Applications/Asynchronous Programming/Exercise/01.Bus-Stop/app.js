function getInfo() {
    let stopIdField = document.getElementById("stopId").value;
    let stopName = document.getElementById("stopName");
    let buses = document.getElementById("buses");
    let req1Url = `http://localhost:3030/jsonstore/bus/businfo/${stopIdField}/name`;
    let req2Url = `http://localhost:3030/jsonstore/bus/businfo/${stopIdField}/buses`;

    request1 = new XMLHttpRequest();
    request2 = new XMLHttpRequest();
    request3 = new XMLHttpRequest();

    request1.addEventListener("readystatechange", function () {
        if (request1.status == 200 && request1.readyState == 4) {
            //resp = request1.responseText.split('"');
            stopName.textContent = request1.responseText;
        }else {
            stopName.textContent = "Error";
            buses.textContent = "";
        }
    });

    request2.addEventListener("readystatechange", function () {
        if (request2.status == 200 && request2.readyState == 4) {
            busesList = document.createElement("ul");
            buses.appendChild(busesList);

            busesForStop = JSON.parse(request2.responseText);

            for(var n in busesForStop){
                entry = document.createElement("li")
                entry.textContent = `Bus ${n} arrives in ${busesForStop[n]} minutes\n`
                busesList.appendChild(entry);
            }
        }
    });

    request1.open("GET", req1Url);
    request1.send();
    request2.open("GET", req2Url);
    request2.send();
}
function solve() {
    departButton = document.querySelector("input[value='Depart']");
    arriveButton = document.querySelector("input[value='Arrive']");
    currentStop = document.querySelector("div#info span.info");
    findNextId = ""

    function depart() {
        if(currentStop.textContent == "Not Connected"){
            findNextId = "Depot";
            fetch("http://localhost:3030/jsonstore/bus/schedule/depot").then((response) => response.json()).then((data) => currentStop.textContent = "Next stop " + data.name);
        }else {
            if(findNextId == "Depot"){
                findNextId = findNextId.toLowerCase();
            }

            fetch(`http://localhost:3030/jsonstore/bus/schedule/${findNextId}`)
            .then((response) => response.json())
            .then((data) => findNextId = data.next);
            //console.log(findNextId);
            fetch(`http://localhost:3030/jsonstore/bus/schedule/${findNextId}`)
            .then((response) => response.json())
            .then((data) => currentStop.textContent = "Next stop " + data.name);
        }

        departButton.setAttribute("disabled", "true");
        arriveButton.removeAttribute("disabled");
    }

    function arrive() {
        let changeTxt = currentStop.textContent.split(" ");
        changeTxt[0] = "Arriving";
        changeTxt[1] = "at";
        currentStop.textContent = changeTxt.join(" ");
        arriveButton.setAttribute("disabled", "true");
        departButton.removeAttribute("disabled");
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
window.addEventListener('load', solve);

function solve() {
    let editMode = false;
    let confirmationPhase = false;

    let editBtn = document.createElement("button");
        editBtn.setAttribute("class", "edit-btn");
        editBtn.textContent = "Edit";

    let continueBtn = document.createElement("button");
    continueBtn.setAttribute("class", "continue-btn");
    continueBtn.textContent = "Continue";

    let nextBtn = document.querySelector("button#next-btn");
    let infolist = document.querySelector("ul.info-list");


    let firstNameField = document.querySelector("input#first-name");
    let lastNameField = document.querySelector("input#last-name");
    let dateInField = document.querySelector("input#date-in");
    let dateOutField = document.querySelector("input#date-out");
    let guestCountField = document.querySelector("input#people-count")

    nextBtn.addEventListener("click", () => {
        nextBtn.setAttribute("disabled", "true");

        if (editMode == false){
            let reservationData = document.createElement("li");
            let articleElem = document.createElement("article");
            let name = document.createElement("h3");
            let from = document.createElement("p");
            let to = document.createElement("p");
            let guests = document.createElement("p");
            reservationData.setAttribute("class", "reservation-content");

            infolist.appendChild(reservationData);
            reservationData.appendChild(articleElem);
            reservationData.appendChild(editBtn);
            reservationData.appendChild(continueBtn);

            articleElem.appendChild(name);
            articleElem.appendChild(from);
            articleElem.appendChild(to);
            articleElem.appendChild(guests);


            name.textContent = "Name: " + firstNameField.value + " " + lastNameField.value;
            from.textContent = "From date: " + dateInField.value;
            to.textContent = "To date: " + dateOutField.value;
            guests.textContent = "For " + guestCountField.value + " people";
        }else {
            let reservationData = document.querySelector("li.reservation-content");
            //let articleElem = document.querySelector("li.reservation-content article");
            let name = document.querySelector("li.reservation-content article h3");
            let PTags = document.querySelectorAll("li.reservation-content article p");
            
            name.textContent = "Name: " + firstNameField.value + " " + lastNameField.value;
            PTags[0].textContent = "From date: " + dateInField.value;
            PTags[1].textContent = "To date: " + dateOutField.value;
            PTags[2].textContent = "For " + guestCountField.value + " people";

            reservationData.style.display = "block";

        }



        firstNameField.value = "";
        lastNameField.value = "";
        dateInField.value = "";
        dateOutField.value = "";
        guestCountField.value = "";

        editMode = false;
        });

    editBtn.addEventListener("click", () => {
        if(confirmationPhase == false){
            editMode = true;

            let name = document.querySelector("li.reservation-content h3").textContent;
            let dataInPtags = document.querySelectorAll("li.reservation-content p");
            let dayIn = dataInPtags[0].textContent.split(": ")[1];
            let dayOut = dataInPtags[1].textContent.split(": ")[1];
            let guests = dataInPtags[2].textContent.split(" ")[1];
            let reservationData = document.querySelector("li.reservation-content");
            reservationData.style.display = "none";


            firstNameField.value = name.split((" "))[1];
            lastNameField.value = name.split(" ")[2];
            dateInField.value = dayIn;
            dateOutField.value = dayOut;
            guestCountField.value = guests;
            nextBtn.removeAttribute("disabled");
        }else {
            let reservationData = document.querySelector("ul.confirm-list li.reservation-content");
            reservationData.remove();

            let success = document.querySelector("h1#verification");
            success.setAttribute("class", "reservation-confirmed");
            success.textContent = "Confirmed";
        }
    });



    continueBtn.addEventListener("click", () => {
        if(confirmationPhase == false){
            confirmationPhase = true;

            let confirmList = document.querySelector("ul.confirm-list");
            let reservationData = document.querySelector("ul.info-list li.reservation-content");
            
            confirmList.appendChild(reservationData);

            editBtn.textContent = "Confirm";
            editBtn.setAttribute("class", "confirm-btn");

            continueBtn.textContent = "Cancel";
            continueBtn.setAttribute("class", "cancel-btn");

        } else {
            let reservationData = document.querySelector("ul.confirm-list li.reservation-content");
            reservationData.remove();

            let cancel = document.querySelector("h1#verification");
            cancel.setAttribute("class", "reservation-cancelled");
            cancel.textContent = "Cancelled";
        }
    });
}



    
    

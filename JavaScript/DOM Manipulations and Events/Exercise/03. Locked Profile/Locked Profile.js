function AttachEvents() {
    let buttons = document.getElementsByTagName('button');
    
    for(var k = 0; k < buttons.length; k++){
        buttons[k].addEventListener("click", AccountsControl);
        buttons[k].setAttribute("id", k+1);
    }



    function AccountsControl() {
        if (this.className == "") {
            this.setAttribute("class", "active");
        }

        let getAccounts = document.querySelectorAll("div.profile");

        for(var j = 0; j < getAccounts.length; j++){

            let lockedOrNot = getAccounts[j].children[2];

            if(getAccounts[j].children[10].className == "active" && getAccounts[j].children[10].id == this.id){

                if(lockedOrNot.checked != true){
                    let dataFields = getAccounts[j].children[getAccounts[j].children.length-2];
                    dataFields.style.display = "block";
                    this.textContent = "Hide it";
                    this.className = "activated";
                }else {
                    this.className = "";
                }

            } else if (getAccounts[j].children[10].className == "activated" && getAccounts[j].children[10].id == this.id){
                    if(lockedOrNot.checked != true){
                    let dataFields = getAccounts[j].children[getAccounts[j].children.length-2];
                    dataFields.style.display = "none";
                    this.className = "";
                    this.textContent = "Show more";
                }
            }
        }
    }
}

AttachEvents();
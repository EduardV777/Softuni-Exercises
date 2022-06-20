function search() {
    let resBox = document.getElementById('result');
    resBox.style.display = "none";

    let searchButton = document.getElementById("searchBtn");
    let searchFieldValue = document.getElementById('searchField').value;
    let table = document.querySelectorAll("table.container tr");
    let pattern = new RegExp(searchFieldValue, "i");

    searchButton.onclick = function () {
        if(resBox.innerHTML == 1) {
            for(var c = 0; c < table.length; c++){
                table[c].setAttribute('class', "");
            }
        }
    
        if(searchFieldValue != ""){
            resBox.innerHTML = 1;
            for(let k = 2; k < table.length; k++){
                let data = table[k].innerText.split("\t");
                
                for(let j = 0; j < data.length; j++){
                    if(data[j].search(pattern) != -1){
                        table[k].classList.add('select');
                        break;
                    }
                }
            }
        }
    }
}

search();
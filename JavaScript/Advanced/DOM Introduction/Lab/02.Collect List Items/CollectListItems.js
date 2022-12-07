function extractText() {
    let listItems = document.querySelectorAll("#items li");
    let textBox = document.getElementById("result");

    let contents = "";
    // console.log(listItems);

    for(let k = 0; k < listItems.length; k++){
        contents += listItems[k].innerText;

        if(k != listItems.length - 1){
            contents += "\n";
        }
    }

    textBox.textContent = contents;

}
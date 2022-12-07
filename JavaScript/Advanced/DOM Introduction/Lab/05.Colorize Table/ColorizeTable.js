function colorize() {
    let table = document.querySelectorAll("table tr");
    
    for(let row = 0; row < table.length; row++){
        if((row + 1) % 2 == 0){
            table[row].style.backgroundColor = "Teal";
        }
    }
}
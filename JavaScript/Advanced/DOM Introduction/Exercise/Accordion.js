function Toggle(){
    // hidden div is with id 'extra'
    let buttonToggle = document.getElementsByClassName('button')[0];
    let contentBox = document.getElementById('extra');
    if(buttonToggle.innerHTML == "More"){
        buttonToggle.innerHTML = "Less";
        contentBox.style.display = 'block';
    }else {
        buttonToggle.innerHTML = "More";
        contentBox.style.display = 'none';
    }
}
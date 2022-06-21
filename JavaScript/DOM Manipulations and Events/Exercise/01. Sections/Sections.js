function create(blocksArray){
    let body = document.getElementsByTagName('body')[0];
    let contentBox = document.getElementById('content');

    let refs = [];

    for(let k = 0; k < blocksArray.length; k++){
        let div = document.createElement("div");
        
        let paragraph = document.createElement('p');
        paragraph.style.display = "none";
        paragraph.textContent = blocksArray[k];

        div.addEventListener("click", ShowText);
        div.appendChild(paragraph);
        refs.push(div);

    }

    for(var e = 0; e < refs.length; e++){
        contentBox.appendChild(refs[e]);
    }


    //event functions
    function ShowText(){
        this.children[0].style.display = "block";
    }

}
function search() {
    let citiesFound = 0;
    let listContent = document.querySelectorAll('ul li');
    let searchFieldValue = document.getElementById("searchText").value;
    let resultBox = document.getElementById('result');
    let pattern = new RegExp(searchFieldValue);
    console.log(pattern);

    if (resultBox.innerHTML != ""){
        for(var k = 0; k<listContent.length; k++){
            listContent[k].style.textDecoration = 'none';
            listContent[k].style.fontWeight = 'normal';
        }
    }

    for(var k = 0; k < listContent.length; k++){
        if(listContent[k].innerHTML.search(searchFieldValue) != -1){
            citiesFound += 1;
            listContent[k].style.textDecoration = 'underline';
            listContent[k].style.fontWeight = 'bold';
        }
    }
    resultBox.innerHTML = citiesFound + " matches found"
}
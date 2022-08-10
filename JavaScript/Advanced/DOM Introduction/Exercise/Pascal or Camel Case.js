function ProcessText(){
    let error = false;
    let btn = document.querySelector('input[type="button"]');
    let spanElement = document.querySelector('div span#result');
    let txtToModify = document.querySelector('input#text').value;
    let caseType = document.querySelector('input#naming-convention').value;
    txtToModify = txtToModify.split(' ');

    if(caseType == "Camel Case"){
        for(var k = 0; k < txtToModify.length; k++){
            let word = txtToModify[k].split('');

            for(var ch = 0; ch < word.length; ch++){
                word[ch] = word[ch].toLowerCase();
            }

            if(k != 0){
                word[0] = word[0].toUpperCase();
            }
            word = word.join('');
            txtToModify[k] = word;
        }
    }else if(caseType == "Pascal Case"){
        for(var k = 0; k < txtToModify.length; k++){
            let word = txtToModify[k].split('');

            for(var ch = 0; ch < word.length; ch++){
                word[ch] = word[ch].toLowerCase();
            }

            word[0] = word[0].toUpperCase();
            word = word.join('');
            txtToModify[k] = word;
        }
    }else {
        error = true;
    }
    
    txtToModify = txtToModify.join('');

    if(error != true){
        spanElement.textContent = txtToModify;
    } else {
        spanElement.textContent = "Error!";
    }
}
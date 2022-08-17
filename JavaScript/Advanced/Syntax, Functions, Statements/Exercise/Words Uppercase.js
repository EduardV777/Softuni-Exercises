function ExtractWords(str){
    let extractedWords = [], currWord = "";
    for(var k = 0; k <= str.length; k++){
        if(k != str.length){
            if((65 <= str[k].charCodeAt(0) && str[k].charCodeAt(0) <= 90) || (97 <= str[k].charCodeAt(0) && str[k].charCodeAt(0) <= 122)){
                currWord += str[k];
            }else if(currWord != ""){
                extractedWords.push(currWord.toUpperCase());
                currWord = "";
            }
        }else if(currWord != ""){
            extractedWords.push(currWord.toUpperCase());
        }
    }

    console.log(extractedWords.join(", "));
}
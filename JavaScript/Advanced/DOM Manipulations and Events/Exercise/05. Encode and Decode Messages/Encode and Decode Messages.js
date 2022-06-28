function Encode() {
    let boxes = document.getElementsByTagName('div');
    let sendTextBox = boxes[1].children[1], receiveBox = boxes[2].children[1];
    let encodeBtn = boxes[1].children, decodeBtn = boxes[2].children;
    encodeBtn = encodeBtn[encodeBtn.length-1], decodeBtn = decodeBtn[decodeBtn.length-1]

    encodeBtn.addEventListener('click', SendMessage);
    decodeBtn.addEventListener('click', DecodeMessage);


    function SendMessage() {

        let textToProcess = sendTextBox.value.split('');

        for(var k = 0; k < textToProcess.length; k++){
            let currChar = textToProcess[k].charCodeAt(0);
            currChar += 1;
            textToProcess[k] = String.fromCharCode(currChar);
        }

       receiveBox.value = textToProcess.join('');
       sendTextBox.value = "";
    }

    function DecodeMessage() {
        let textToProcess = receiveBox.value.split('');

        if(textToProcess.length > 0){
            for(var k = 0; k < textToProcess.length; k++){
                let currChar = textToProcess[k].charCodeAt(0);
                currChar -= 1;
                textToProcess[k] = String.fromCharCode(currChar);
            }

            receiveBox.value = textToProcess.join('');
        }
    }
}

Encode();

//The password for my bank account is 123pass321
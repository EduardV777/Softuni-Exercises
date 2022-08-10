function validateHttpRequest(requestObject) {
    let valid = true, optionIdx = -1, errorType = "";

    if(CheckForAllRequiredProperties() == false){
        valid = false;
    }else {
        CheckDoTheyFulfillCriteria();
    }



    if(valid == true){
        return requestObject;
    }else {
        throw new Error(`Invalid request header: Invalid ${errorType}`);
    }


    function CheckDoTheyFulfillCriteria() {
        for(let option in requestObject) {
            optionIdx++;

            if(optionIdx == 0){

                if (option == "method"){
                    if(requestObject[option] != "GET" && requestObject[option] != "POST" && requestObject[option] != "DELETE" && requestObject[option] && "CONNECT"){
                        valid = false;
                        errorType = "Method"
                        break;
                    }
                }

            }else if (optionIdx == 1){
                if(option == "uri"){

                    let pattern = new RegExp('^([\\w])+(\\.){1}([\\w])$');

                    if(requestObject[option] == "" || requestObject[option].search(pattern) == -1){
                        valid = false;
                        errorType = "URI";
                        break;
                    }
                }
            }else if(optionIdx == 2){
                if(option == "version"){
                    if(requestObject[option] != "HTTP/0.9" && requestObject[option] != "HTTP/1.0" && requestObject[option] != "HTTP/1.1" && requestObject[option] != "HTTP/2.0"){
                        valid = false;
                        errorType = "Version";
                        break;
                    }
                }
            }else if(optionIdx == 3){
                if(option == "message"){
                    let pattern = new RegExp("[<|>|\|'|\"|&]+");
                    if(requestObject[option].search(pattern) != -1){
                        valid = false;
                        errorType = "Message";
                        break;
                    }
                }
            }
        }
    }

    function CheckForAllRequiredProperties() {
        let methodExists = "method" in requestObject;
        let uriExists = "uri" in requestObject;
        let versionExists = "version" in requestObject;
        let messageExists = "message" in requestObject;

        if(methodExists == true && uriExists == true && versionExists == true && messageExists == true){
            return true;
        }else {
            if(methodExists == false){
                errorType = "Method";
            }
            if (uriExists == false ){
                errorType = "URI";
            }
            if (versionExists == false){
                errorType = "Version";
            }
            if(messageExists == false){
                errorType = "Message";
            }
            return false;
        }

    }
}



console.log(validateHttpRequest({
    method: 'GET',
    uri: 'svn.public.catalog',
    version: 'HTTP/1.1',
    message: ''
}));


//method, uri, version , message



//expected input
/*
{
    method: 'GET',
    uri: 'svn.public.catalog',
    version: 'HTTP/1.1',
    message: ''
  }

  */
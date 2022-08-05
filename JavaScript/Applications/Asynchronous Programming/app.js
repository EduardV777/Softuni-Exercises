var url = "https://testproj-dcb4c-default-rtdb.europe-west1.firebasedatabase.app/.json";

function loadRepos() {

    var httpRequest = new XMLHttpRequest();

    httpRequest.addEventListener("readystatechange", function () {
        if (httpRequest.readyState == 4 && httpRequest.status == 200) {
            document.getElementById("res").innerHTML = httpRequest.responseText;
        }
    });

    httpRequest.open("GET", url);
    httpRequest.send();
}

function addResource(){
    var requestContent = '[{"Mazda": "RX-5"}, {"BMW": "M3"}, {"Ferrari": "458 Italia"}]';
    var httpPost = new XMLHttpRequest();

    httpPost.addEventListener("readystatechange", function() {
        if(httpPost.readyState == 4 && httpPost.status == 200){
            alert('The resources were updated!');
            loadRepos();
        }else if(httpPost.readyState == 2 || httpPost.readyState == 1 || httpPost.readyState == 3){
            alert("Data loading...");
        }else {
            alert("Data was not sent!\n"+httpPost.responseText);
        }
    });

    httpPost.open("POST", url);
    httpPost.send(requestContent);
}
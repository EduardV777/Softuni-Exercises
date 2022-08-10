let newText = document.createElement('p');
let hr1 = document.createElement('hr');
let hr2 = document.createElement('hr');

let getBody = document.getElementsByTagName("body")[0];

newText.innerHTML = "<b>New text added</b>";

getBody.appendChild(newText);
getBody.prepend(hr1);
getBody.append(hr2);
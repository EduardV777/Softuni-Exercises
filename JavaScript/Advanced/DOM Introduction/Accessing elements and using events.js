var body = document.getElementsByTagName('body');
var pTags = document.getElementsByTagName('p');
var randClassElements = document.getElementsByClassName('rand');
var spanElement = document.querySelector('span.rand');
var txt1 = document.getElementById("txt1");

txt1.onclick = function() {
    txt1.innerHTML = "<b>Action detected</b>";
}

//Converting to array
//pTagsArray = Array.from(pTags)

//console.log(body[0].firstChild);
console.log(pTags);
//console.log(pTagsArray);
console.log(randClassElements);
console.log(spanElement);
console.log(spanElement.parentElement);
console.log(txt1);
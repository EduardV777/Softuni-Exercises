function showText() {
  var textToShow=document.getElementById('text');
  var readMore=document.getElemenyById('more');
  readMore.onclick=function(){
    textToShow.style.display='inline';
  }
}

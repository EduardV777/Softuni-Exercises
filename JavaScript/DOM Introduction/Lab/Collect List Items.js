function scanAndAppend(){
  var list=document.getElementsByTagName('ul');
  var txtBox=document.getElementsByTagName('textarea');
  //console.log(list[0].textContent);
  txtBox[0].textContent=list[0].textContent;
}

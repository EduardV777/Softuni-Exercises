function edit(HTMLref, match, replacer){
  var content=HTMLref.textContent;
  var find=new RegExp(match, 'g');
  var edited=content.replace(find, replacer);
  HTMLref.textContent=edited;
}

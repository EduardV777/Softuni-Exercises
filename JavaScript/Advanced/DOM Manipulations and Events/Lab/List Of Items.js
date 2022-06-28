function addItem() {
  //input field id: newItemText / list ID: items
  var list=document.getElementById("items");
  var inputField=document.getElementById('newItemText');
  var text=inputField.textContent;
  inputField.appendChild(text);
}

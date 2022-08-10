function addItem() {
    let textField = document.getElementById("newItemText");
    let valueField = document.getElementById('newItemValue');
    let menu = document.getElementById("menu");

    let text = textField.value, value = valueField.value;
    textField.value = "", valueField.value = "";

    let newItem = document.createElement('option');
    newItem.textContent = text, newItem.value = value;

    menu.appendChild(newItem);
}
function solve() {
    let buttonsOnPage = document.getElementsByTagName('button');
    let generateBtn = buttonsOnPage[0], buyBtn = buttonsOnPage[1];
    let furnitureTable = document.querySelector('table tbody');
    let textBoxes = document.getElementsByTagName('textarea');
    let orderBox = textBoxes[0], buyBox = textBoxes[1];

    generateBtn.addEventListener('click', genButtonAction);
    buyBtn.addEventListener('click', buyButtonAction);

    function genButtonAction() {
        let orderBoxValue = orderBox.value;

        orderBoxValue = JSON.parse(orderBoxValue);
        
        for(var k = 0; k < orderBoxValue.length; k++){
            let newRow = document.createElement('tr'), imgCell = document.createElement('td'), nameCell = document.createElement('td'), priceCell = document.createElement('td'), decFactorCell = document.createElement('td'), markCell = document.createElement('td');
            imgCell.innerHTML = "<img src='"+orderBoxValue[k]['img']+"'>";
            nameCell.innerHTML = "<p>"+orderBoxValue[k]['name']+"</p>";
            priceCell.innerHTML = "<p>"+orderBoxValue[k]['price']+"</p>";
            decFactorCell.innerHTML = "<p>"+orderBoxValue[k]['decFactor']+"</p>";
            markCell.innerHTML = "<input type='checkbox'>";

            newRow.appendChild(imgCell), newRow.appendChild(nameCell), newRow.appendChild(priceCell), newRow.appendChild(decFactorCell), newRow.appendChild(markCell);
            furnitureTable.appendChild(newRow);
        }
    }

    function buyButtonAction() {
        let output = `Bought furniture: `, total = 0, decFactorValue = 0;
        let checkboxes = document.querySelectorAll("input[type='checkbox']");
        let records = document.querySelectorAll("tbody tr")
        let itemsBought = 0;

        for(var j = 0; j < checkboxes.length; j++){

            if(checkboxes[j].disabled == false){
                itemsBought++;
                checkboxes[j].checked = true;
                output += `${records[j].children[1].children[0].textContent}`;
                total += Number(records[j].children[2].children[0].textContent);
                decFactorValue += Number(records[j].children[3].children[0].textContent);

                if(j != checkboxes.length - 1){
                    output += ", ";
                }
            }

        }

        decFactorValue /= itemsBought;
        output += `\nTotal price: ${total.toFixed(2)}\nAverage decoration factor: ${decFactorValue}`;
        
        buyBox.value = output;
    }
}


//.\nTotal price: ${}\n Average decoration factor: ${}`
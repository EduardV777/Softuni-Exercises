function Subtract() {
    let num1 = document.getElementById('firstNumber').value;
    let num2 = document.getElementById('secondNumber').value;
    let resBox = document.querySelector("div#result");

    resBox.innerHTML = Number(num1) - Number(num2);
}

Subtract();
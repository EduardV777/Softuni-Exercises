function calc() {
    let num1 = Number(document.getElementById("num1").value);
    let num2 = Number(document.getElementById("num2").value);

    let sumField = document.getElementById("sum");

    sumField.value = num1 + num2;
}

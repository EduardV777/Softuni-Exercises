let numArr = ["carbonara", "pizza", "potatoes", "soup"];

console.log(numArr.splice(0, 2, "12"));
console.log(numArr);
console.log(numArr.splice(0, 1, "SUV"));
console.log(numArr);
console.log(numArr.splice(0, 1, "Bus", "Truck"));
console.log(numArr);

console.log("");


let tools = ["hammer", "screwdriver", "shovel"];

console.log(tools);
tools.fill("ham", 0, 1);
console.log(tools);
tools.fill("candybar", 0, 3);
console.log(tools);
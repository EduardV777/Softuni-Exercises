numbers = [1,2,3,4,5,6];

function MultiplyByTen(element, index, arr){
    arr[index] = element * 10;
}

function DivideByThree(item){
    return item / 3;
}

function IsItLow(item){
    if(item <= 30){
        return true;
    }else {
        return false;
    }
}

function concatenate(prevVal, currVal){
    return String(prevVal) + String(currVal);
}

console.log("forEach()");
console.log(numbers);
numbers.forEach(MultiplyByTen);
console.log(numbers);

console.log("map()")

numbers2 = numbers.map(DivideByThree);

console.log(numbers2);
console.log(numbers);

console.log("some()");

console.log(numbers.some(IsItLow) + "\nsplice()-ing the array");

numbers.splice(0, 3)
console.log(numbers);
console.log(numbers.some(IsItLow));



console.log("reduce()");

let res = numbers.reduce(concatenate, "");

console.log(res);


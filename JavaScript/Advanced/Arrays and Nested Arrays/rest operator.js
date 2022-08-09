function Sum(...args){
    let sum = 0;
    for(var k = 0; k < args.length; k++){
        sum += args[k];
    }

    return sum;
}

console.log(Sum(1,2));

console.log(Sum(2,2,3));

console.log(Sum(2,2,2,2,2));

//unpacking elements

let numbers = [20,30,45,2,123,213];
let [a, b, c, ...restNums] = numbers;
console.log("Array 'numbers': " + numbers);
console.log("Unpacked elements");
console.log(a);
console.log(b);
console.log(c);
console.log(restNums);
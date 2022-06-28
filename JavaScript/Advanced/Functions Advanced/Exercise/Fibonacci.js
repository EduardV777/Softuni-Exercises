function FibonacciSequence() {
    let a = 0, b = 1, start = false;
    return function() { let result = a + b; if(start == true) { a = b }else { start = true } b = result ; return result; }
}

let fib = FibonacciSequence();

console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
console.log(fib());
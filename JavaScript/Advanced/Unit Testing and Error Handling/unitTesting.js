let assert = require('chai');
let multiply = require("./Multiplication");

describe('testResults', function() {
    //must pass
    it('testMultiplicationResult', () => { assert.assert.equal(multiply(4,5), 20)});
    it('ZeroAndZeroMakesZero', () => assert.assert.equal(multiply(0,0), 0));
    it('MinusPlusMakesMinus', () => assert.assert.equal(multiply(-1,1), -1));
    //must fail
    it('WrongResults', () => assert.assert.equal(multiply(2,3), 10));
});
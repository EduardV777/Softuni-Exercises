let assert = require('chai');
let motorcycleRider = require("./Motorcycle Rider")

describe("Tests …", function() {
    describe("licenseRestriction", function() {
        it('IfCategoryAm', () => { assert.assert.equal(motorcycleRider.licenseRestriction("AM"),'Mopeds with a maximum design speed of 45 km. per hour, engine volume is no more than 50 cubic centimeters, and the minimum age is 16.')});
        it("IfCategoryA1", () => { assert.assert.equal(motorcycleRider.licenseRestriction("A1"), "Motorcycles with engine volume is no more than 125 cubic centimeters, maximum power of 11KW. and the minimum age is 16.")});
        it("IfCategoryA2", () => { assert.assert.equal(motorcycleRider.licenseRestriction("A2"), "Motorcycles with maximum power of 35KW. and the minimum age is 18.")});
        it("IfCategoryA", () => { assert.assert.equal(motorcycleRider.licenseRestriction("A"), "No motorcycle restrictions, and the minimum age is 24.")});
        it("IfAnythingElse", () => { assert.assert.throws(motorcycleRider.licenseRestriction("R"), "Invalid Information!")})
    });
    describe("motorcycleShowroom", function(){
        it("EngineLimits", () => { assert.assert.equal(motorcycleRider.motorcycleShowroom([125, 250, 600, 400], 500), "There are 3 available motorcycles matching your criteria!") });
        it("WrongFirstArgument", () => { assert.assert.throws(motorcycleRider.motorcycleShowroom("[200,300]", "wow"), "Invalid Information!")});
        it("WrongSecondArgument", () => { assert.assert.throws(motorcycleRider.motorcycleShowroom([200,300], "wow"), "Invalid Information!")});
    });
    describe("otherSpendings", function() {
        it("FailIf", () => assert.assert.throws(motorcycleRider.otherSpendings("lol", ["engine oil"], false), errorInstance, "Invalid Information!"));
        it("FailIf2", () => assert.assert.throws(motorcycleRider.otherSpendings(["helmet"], "lol", true), errorInstance, "Invalid Information!"));
        it("FailIf3", () => assert.assert.throws(motorcycleRider.otherSpendings(["helmet"], ["engine oil"], "nodiscount"), "Invalid Information!"));
        it("FailIf3", () => assert.assert.throws(motorcycleRider.otherSpendings(["helmet"], ["engine oil"], "nodiscount"), "Invalid Information!"));
        it("CorrectMessage", () => assert.assert.equal(motorcycleRider.otherSpendings(["helmet"], ["engine oil"], false), "You spend $270.00 for equipment and consumables!"));
        it("CorrectMessage2", () => assert.assert.equal(motorcycleRider.otherSpendings(["helmet"], ["engine oil"], true), "You spend $243.00 for equipment and consumables with 10% discount!"));
    });

    });
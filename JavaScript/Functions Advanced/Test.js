arr = ["I"," Love", " Cookies"];
arr2 = [1,2,123,200];
let result = 0;

console.log(arr.reduceRight(function(a,x){ return x+a}, ""));

result = arr2.reduce(function(x,res){ return res+x }, result);

console.log(result);

//

let playerData = {name: 'EdwardV777', points: 1270, favoriteGame: "8 Ball Pool"};


function getPoints() {
    return this.points;
}

function getPlayerName() {
    return this.name;
}

function getFavoriteGame() {
    return this.favoriteGame;
}

console.log(getPoints());
console.log(getPoints.call(playerData));

getPlayerName = getPlayerName.bind(playerData);
console.log(getPlayerName());

console.log(getFavoriteGame.apply(playerData));


//

users = [{ name: 'Tim', age: 25}, { name: 'Sam', age: 390}, { name: 'Bill', age: 200}];
console.log(users);
let getName = (user) => user.name;
//console.log(typeof(getName));
usernames = users.map(getName);
console.log(usernames);

let show = () => "text";

console.log(typeof(show));


function sum3(a) {
    return (b) => {
        return (c) => {
            return a + b + c;
        }
    }
}

console.log(sum3(5)(5)(5));
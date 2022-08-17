<<<<<<< HEAD
// function ComposeObjects(funcLibrary, orders) {
//   let objects=[]
//   console.log(orders.parts)
//   for(var k in orders.parts){
//     console.log(orders.parts[k]);
//     objects.push(funcLibrary.k(orders.template));
//   }
//   return objects;
// }
//
//
// const library = {
// print: function () {
// console.log(`${this.name} is printing a page`);
// },
// scan: function () {
// console.log(`${this.name} is scanning a document`);
// },
// play: function (artist, track) {
// console.log(`${this.name} is playing '${track}' by ${artist}`);
// },
// };
// const orders = [
// {
// template: { name: 'ACME Printer'},
// parts: ['print']
// },
// {
// template: { name: 'Initech Scanner'},
// parts: ['scan']
// },
// {
// template: { name: 'ComTron Copier'},
// parts: ['scan', 'print']
// },
// {
// template: { name: 'BoomBox Stereo'},
// parts: ['play']
//   }
// ];
// ComposeObjects(library, orders);
=======
function factory(libraryFunc, ordersArr){
    let completedOrders = [];

    for(var k = 0; k < ordersArr.length; k++){
        let name = ordersArr[k].template.name;
        let currOrder = {name};

        for(var j of ordersArr[k].parts){
            for(var key in libraryFunc){
                if(key == j){
                    console.log(j);
                    currOrder[`${j}`] = libraryFunc[j];
                    break
                }
            }
        }
        completedOrders.push(currOrder);
    }

    return completedOrders;
}

// const library = {
//     print: function () {
//       console.log(`${this.name} is printing a page`);
//     },
//     scan: function () {
//       console.log(`${this.name} is scanning a document`);
//     },
//     play: function (artist, track) {
//       console.log(`${this.name} is playing '${track}' by ${artist}`);
//     },
//   };
//   const orders = [
//     {
//       template: { name: 'ACME Printer'},
//       parts: ['print']      
//     },
//     {
//       template: { name: 'Initech Scanner'},
//       parts: ['scan']      
//     },
//     {
//       template: { name: 'ComTron Copier'},
//       parts: ['scan', 'print']      
//     },
//     {
//     template: { name: 'BoomBox Stereo'},
//     parts: ['play']      
//   }
// ];
// const products = factory(library, orders);
// console.log(products);


//const factory = result;

const library = {
    get1: function () {
        return 1;
    },
    get3: function () {
        return 3;
    },
};

const orders = [
    {
        template: {},
        parts: ['get1']
    },
    {
        template: {},
        parts: ['get1', 'get3']
    },
];

const products = factory(library, orders);
console.log(products);
>>>>>>> a796fc383b6d7a1e2b40c52280ee5f85b44360db

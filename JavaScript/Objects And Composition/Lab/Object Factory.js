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

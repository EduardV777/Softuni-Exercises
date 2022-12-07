class OnlineShop {
    constructor(warehouseSpace){
        this.warehouseSpace = warehouseSpace;
        this.products = new Array();
        this.sales = new Array();
    }

    loadingStore(product, quantity, spaceRequired){
        if(this.warehouseSpace <= spaceRequired){
            throw "Not enough space in the warehouse.";
        } else {
            let productObj = {product: product, quantity: quantity};
            this.products.push(productObj);
            this.warehouseSpace -= spaceRequired;
            return `The ${product} has been successfully delivered in the warehouse.`
        }
    }

    quantityCheck(product, minimalQuantity){
        let productFound = false;

        if(minimalQuantity <= 0){
            throw "The quantity cannot be zero or negative.";
        }

        for(let p of this.products){
            if(p.product == product){
                productFound = true;
                if(p.quantity >= minimalQuantity){
                    return `You have enough from product ${product}.`
                }else {
                    let currentQty = p.quantity;
                    p.quantity = minimalQuantity;
                    return `You added ${minimalQuantity - currentQty} more from the ${product} products.`;
                }
            }
        }

        if(productFound == false){
            throw `There is no ${product} in the warehouse.`
        }
    }

    sellProduct(product){
        let productFound = false;

        for(let p of this.products){

            if(p.product == product){
                productFound = true;
                p.quantity -= 1;

                let sale = {product: p.product, quantity: 1};
                this.sales.push(sale);
                return `The ${product} has been successfully sold.`;
            }
        }

        if(productFound == false){
            throw `There is no ${product} in the warehouse.`;
        }
    }


    revision(){
        let output = "";

        if(this.sales.length == 0){
            throw "There are no sales today!";
        }else {
            output += `You sold ${this.sales.length} products today!\n`;
            output += "Products in the warehouse:\n";
            for(let p of this.products){
                output += `${p.product}-${p.quantity} more left\n`;
            }
        }

        return output;
    }
}


// const myOnlineShop = new OnlineShop(500)
// console.log(myOnlineShop.loadingStore('headphones', 10, 200));
// console.log(myOnlineShop.loadingStore('laptop', 5, 200));
// console.log(myOnlineShop.loadingStore('TV', 40, 500));


// const myOnlineShop = new OnlineShop(500)
// console.log(myOnlineShop.loadingStore('headphones', 10, 200));
// console.log(myOnlineShop.loadingStore('laptop', 5, 200));
// console.log(myOnlineShop.quantityCheck('headphones', 10));
// console.log(myOnlineShop.quantityCheck('laptop', 10));
// console.log(myOnlineShop.quantityCheck('TV', 40,));


// const myOnlineShop = new OnlineShop(500)
// console.log(myOnlineShop.loadingStore('headphones', 10, 200));
// console.log(myOnlineShop.loadingStore('laptop', 5, 200));
// console.log(myOnlineShop.quantityCheck('headphones', 10));
// console.log(myOnlineShop.quantityCheck('laptop', 10));
// console.log(myOnlineShop.sellProduct('headphones'));
// console.log(myOnlineShop.sellProduct('laptop'));
// console.log(myOnlineShop.sellProduct('keyboard'));

const myOnlineShop = new OnlineShop(500)
console.log(myOnlineShop.loadingStore('headphones', 10, 200));
console.log(myOnlineShop.loadingStore('laptop', 5, 200));
console.log(myOnlineShop.quantityCheck('headphones', 10));
console.log(myOnlineShop.quantityCheck('laptop', 10));
console.log(myOnlineShop.sellProduct('headphones'));
console.log(myOnlineShop.sellProduct('laptop'));
console.log(myOnlineShop.revision());
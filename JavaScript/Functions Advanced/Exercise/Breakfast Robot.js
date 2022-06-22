function solution() {
    //Carbohydrates, flavour , protein, fat
    const meals = {apple: [1, 2], lemonade: [10, 20], burger: [5, 3, 0, 7], eggs: [0, 1, 5, 1], turkey: [10, 10, 10, 10]};
    let ingredients = {carbohydrate: 0, flavour: 0, protein: 0, fat: 0};

    return function() {

        command = arguments[0].split(" ");
        
        if(command[0] == "restock"){
            if(command[1] in ingredients) {
                command[2] = Number(command[2]);
                ingredients[command[1]] += command[2];
                return 'Success';
            }
        }else if(command[0] == "prepare"){
            let cannotPrepare = false, lackingIngredient = "";

            if(command[1] in meals){
                let requiredIngredients = meals[command[1]];

                for(let k = 0; k < requiredIngredients.length; k++){
                    if(cannotPrepare == true) {
                        break;
                    }

                    if(k == 0){
                        if(ingredients['carbohydrate'] < requiredIngredients[k]*command[2]){
                            cannotPrepare = true, lackingIngredient += 'carbohydrate';
                        } else {
                            ingredients['carbohydrate'] -= requiredIngredients[k] * command[2];
                        }

                    }else if(k == 1){
                        if(ingredients['flavour'] < requiredIngredients[k] * command[2]){
                            cannotPrepare = true, lackingIngredient += 'flavour';
                        }else {
                            ingredients['flavour'] -= requiredIngredients[k] * command[2];
                        }

                    }else if(k == 2){
                        if(ingredients['protein'] < requiredIngredients[k] * command[2]){
                            cannotPrepare = true, lackingIngredient += 'protein';
                        } else {
                            ingredients['protein'] -= requiredIngredients[k] * command[2];
                        }

                    }else if(k == 3){
                        if(ingredients['fat'] < requiredIngredients[k] * command[2]){
                            cannotPrepare = true, lackingIngredient += 'fat';
                        }else {
                            ingredients['fat'] -= requiredIngredients[k] * command[2];
                        }

                    }
                }

                if(cannotPrepare == true) {
                    return `Error: not enough ${lackingIngredient} in stock`;
                } else {
                    return `Success`;
                }
            }
        }else if(command[0] == "report"){
            return `protein=${ingredients['protein']} carbohydrate=${ingredients['carbohydrate']} fat=${ingredients['fat']} flavour=${ingredients['flavour']}`;
        }else {
            //
        }
    }
}







let manager = solution() ;
console.log (manager ("restock flavour 50"));
console.log (manager ("prepare lemonade 4"));
console.log (manager ("restock carbohydrate 10"));
console.log (manager ("restock flavour 10"));
console.log (manager ("prepare apple 1"));
console.log (manager ("restock fat 10"));
console.log (manager ("prepare burger 1"));
console.log (manager ("report"));
/*
restock flavour 50
prepare lemonade 4
restock carbohydrate 10
restock flavour 10
*/

//Commands
// restock <microelement> <qty>
// prepare <recipe> <qty>
// report

//meals
/*

 apple - made with 1 carbohydrate and 2 flavour
 lemonade - made with 10 carbohydrate and 20 flavour
 burger - made with 5 carbohydrate, 7 fat and 3 flavour
 eggs - made with 5 protein, 1 fat and 1 flavour
 turkey - made with 10 protein, 10 carbohydrate, 10 fat and 10 flavour

*/
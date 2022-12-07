function findBiggestElement(matrixArr){
    let num = "none";

    for(let k = 0; k < matrixArr.length; k++){
        for(let j = 0; j < matrixArr[k].length; j++){
            if(num < matrixArr[k][j] || num == "none"){
                num = matrixArr[k][j];
            }
        }
    }

    console.log(num);
}

findBiggestElement([[20, 50, 10],[8, 33, 145]]);
findBiggestElement([[3, 5, 7, 12], [-1, 4, 33, 2], [8, 3, 0, 4]]);
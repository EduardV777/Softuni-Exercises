function processOddPositions(arr){
    let oddPosNumbers = new Array();

    for(let k = 0; k < arr.length; k++){
        if(k % 2 != 0){
            oddPosNumbers.push(arr[k] * 2);
        }
    }

    oddPosNumbers.reverse();

    console.log(oddPosNumbers.join(" "));
}

processOddPositions([10, 15, 20, 25]);
processOddPositions([3, 0, 10, 4, 7, 3]);
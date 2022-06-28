function SortValues(arrToSort, sortType) {

    if(sortType == "asc"){
        arrToSort.sort((a, b) => a - b);
    } else if (sortType == "desc"){
        arrToSort = arrToSort.sort((a, b) => b - a);
    }

    return arrToSort;
}

console.log(SortValues([14, 7, 17, 6, 8], 'desc'));
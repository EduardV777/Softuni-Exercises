function add(num1) {

    return (num2) => {
        return (num3) => {
            if(typeof(num2) == 'undefined'){
                num2 = 0;
            }
            if(typeof(num3) == 'undefined'){
                num3 = 0
            }

            return num1+num2+num3;
        }
    }
}

console.log(add(1)(2));
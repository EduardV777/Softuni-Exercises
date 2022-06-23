invalidError = new Error();
invalidError.name = "Invalid input", invalidError.message = "The parameters are of incorrect type!";



function add(a,b){

    try{
        if(typeof(a) != 'number' || typeof(b) != 'number'){
            throw invalidError;
        }

        let res = a + b;
        console.log(`${a} + ${b} = ${a+b}`);
    }
    catch (err){
        console.error(err.stack);
    }
}


add(5,2);
add(12,12);
add(2);
add("someNum", "notANum");
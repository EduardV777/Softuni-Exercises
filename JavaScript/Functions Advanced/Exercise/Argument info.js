function displayParameterInfo(){
    argumentsTotal = {};
    for(var k of arguments){
        
        if(typeof(k) in argumentsTotal){
            argumentsTotal[typeof(k)]++;
        }else {
            argumentsTotal[typeof(k)] = 1;
        }
        
        console.log(`${typeof(k)}: ${k}`);
    }
    
    argumentsTotal = Array.from([Object.keys(argumentsTotal), Object.values(argumentsTotal)]);

    for(let k = 0; k < argumentsTotal[0].length; k++){
        argumentsTotal[0][k] = [argumentsTotal[0][k], argumentsTotal[1][k]];
    }
    argumentsTotal.pop();

    SortSummary.call(argumentsTotal);
    ShowSummary = ShowSummary.bind(argumentsTotal);
    
    ShowSummary();

    //
    function SortSummary() {

        for(let i = 0; i <= this[0].length - 2; i++){
            
            for(let j = 0; j <= this[0].length - 2; j++){

                if(this[0][j][1] < this[0][j+1][1]){
                    let temp = this[0][j+1];
                    this[0][j+1] = this[0][j];
                    this[0][j] = temp;
                }

            }
        }
    }

    function ShowSummary() {
        for(let k = 0; k < this[0].length; k++){
            console.log(this[0][k].join(" = "));
        }
    }
    
}


displayParameterInfo('dog', 'cat', 42,  function () { console.log('Hello world!'); });
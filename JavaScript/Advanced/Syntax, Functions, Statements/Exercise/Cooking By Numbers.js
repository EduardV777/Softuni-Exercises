function CookingNumbers(number, op1, op2, op3, op4, op5, op6){
  number=Number(number);
  listOfOperations=[op1,op2,op3,op4,op5,op6];
  for(var k in listOfOperations){
    var op=listOfOperations[k];
    if(op=="chop"){
      number/=2;
    }else if(op=="dice"){
      number=Math.sqrt(number);
    }else if(op=="spice"){
      number+=1;
    }else if(op=="bake"){
      number*=3;
    }else if(op=="fillet"){
      number-=(number*0.2);
    }else {
      break;
    }
    console.log(number);
  }
}

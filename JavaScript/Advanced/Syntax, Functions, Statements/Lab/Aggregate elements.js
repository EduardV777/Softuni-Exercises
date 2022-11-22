function ProcessArray(arr){

  function Sum(inverse = false){
      let sum = 0;

      if(inverse == false){
          for(let k = 0; k < arr.length; k++){
              sum += arr[k];
          }
      }else {
          for(let k = 0; k < arr.length; k++){
              sum += 1 / arr[k];
          }
      }

      return sum;
  }

  function Concat(){
      let str = "";

      for(let k = 0; k < arr.length; k++){
          str += String(arr[k]);
      }

      return str;
  }

  console.log(Sum());
  console.log(Sum(true));
  console.log(Concat());
}


ProcessArray([1, 2, 3]);
console.log("--------------------");
ProcessArray([2, 4, 8, 16]);
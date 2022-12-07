function generateSequence(n, k){
  let sequence = [];

  for(let j = 0; j < n; j++){
      if(j == 0){
          sequence.push(1);
      } else {
          
          let sum = 0;

          for(let i = j - 1; i > j - 1 - k; i--){

              if(i < 0){
                  break;
              }
              sum += sequence[i];
          }

          sequence.push(sum);
      }
  }

  return sequence;
}


console.log(generateSequence(6, 3));
console.log(generateSequence(8, 2));
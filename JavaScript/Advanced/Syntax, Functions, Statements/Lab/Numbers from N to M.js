function sumSequence(n, m){
  n = Number(n);
  m = Number(m);
  let sum = 0;

  for(let start = n; start <= m; start++){
      sum += start;
  }

  return sum;
}


console.log(sumSequence('1', '5'));
console.log(sumSequence('-8', '20'));
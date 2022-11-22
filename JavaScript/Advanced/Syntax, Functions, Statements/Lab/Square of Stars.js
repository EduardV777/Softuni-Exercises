function DrawStarRectangle(size = 5){
  let rect = "";

  for(let k = 0; k < size; k++){
      rect += "* ".repeat(size);
      if(k != size - 1){
          rect += "\n";
      }
  }

  console.log(rect);
}

DrawStarRectangle(1);
DrawStarRectangle(2);
DrawStarRectangle(5);
DrawStarRectangle(7);
console.log("\n\nTesting default argument...");

DrawStarRectangle();
function CalcArea(arg){
  if(typeof(arg)=="number"){
    var r=arg;
    var circleArea=Math.pow(r,2)*Math.PI;
    console.log(circleArea.toPrecision(4));
  }else{
    console.log("We can not calculate the circle area, because we receive a "+typeof(arg)+".")
  }
}

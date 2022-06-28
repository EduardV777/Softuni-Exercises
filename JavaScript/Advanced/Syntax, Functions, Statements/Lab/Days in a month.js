function GetDays(month,year){
  var time=new Date(year,month-1), maxDay=28, currMonth=time.getMonth();
  while(currMonth==time.getMonth()){
    time.setDate(maxDay+1);
    if(currMonth==time.getMonth()){
      maxDay+=1;
    }
  }
  return maxDay;
}

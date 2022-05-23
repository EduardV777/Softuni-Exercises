function FindOutPreviousDay(year, month, day){
  if(day==1){
    if(month-1==9){
      day-=1;
    }
  }
  yesterday=new Date(year,month,day-1);
  console.log(yesterday.getFullYear()+"-"+yesterday.getMonth()+"-"+yesterday.getDate());
}

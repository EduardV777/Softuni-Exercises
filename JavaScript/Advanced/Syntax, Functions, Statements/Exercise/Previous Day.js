function findPreviousDay(year, month, day){
    
  let dateObj = new Date(year, month - 1, day);
  
  function printDate(){
      console.log(`${dateObj.getFullYear()}-${dateObj.getMonth() + 1}-${dateObj.getDate()}`);
  }
  
  dateObj.setDate(dateObj.getDate() - 1);
  
  printDate();
}

findPreviousDay(2016, 3, 1);
findPreviousDay(2016, 9, 30);
findPreviousDay(2016, 10, 1);
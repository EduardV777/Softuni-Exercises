function getDaysInMonth(month, year){
  let dateObj = new Date(year, month - 1);
  let daysInMonth;

  if(dateObj.getMonth() == 1){
      if(year % 4 == 0){
          daysInMonth = 29;
      }else {
          daysInMonth = 28;
      }

  } else {
      switch(dateObj.getMonth()){
          case 3:
          case 5:
          case 8:
          case 10:
              daysInMonth = 30;
              break;
          
          case 0:
          case 2:
          case 4:
          case 6:
          case 7:
          case 9:
              daysInMonth = 31;
              break;
      }
  }

  console.log(daysInMonth);
}

getDaysInMonth(1, 2012);
getDaysInMonth(2, 2021);
getDaysInMonth(2, 2020);
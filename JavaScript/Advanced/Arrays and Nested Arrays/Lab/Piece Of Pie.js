function returnFlavors(arr, flavor1, flavor2){
  let newFlavors = new Array();
  let start = false;

  for(let k = 0; k < arr.length; k++){
      if(arr[k] == flavor1){
          newFlavors.push(arr[k]);
          start = true;

      }else if (arr[k] == flavor2) {
          newFlavors.push(arr[k]);
          break;
          
      } else {
          if(start == true){
              newFlavors.push(arr[k]);
          }
      }
  }

  return newFlavors;
}





console.log(returnFlavors(['Pumpkin Pie', 'Key Lime Pie', 'Cherry Pie', 'Lemon Meringue Pie', 'Sugar Cream Pie'], 'Key Lime Pie', 'Lemon Meringue Pie'));

console.log(returnFlavors(['Apple Crisp', 'Mississippi Mud Pie', 'Pot Pie', 'Steak and Cheese Pie', 'Butter Chicken Pie', 'Smoked Fish Pie'], 'Pot Pie', 'Smoked Fish Pie'));
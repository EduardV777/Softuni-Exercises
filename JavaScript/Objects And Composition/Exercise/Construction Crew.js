function ModifyObject(workerObject) {
    if(workerObject.dizziness == true){
      requiredWater = 0
      requiredWater += 0.1*workerObject.weight*workerObject.experience;
      workerObject.levelOfHydrated += requiredWater;
      workerObject.dizziness = false;
    }

    return workerObject;
}


ModifyObject({ weight: 120,
experience: 20,
levelOfHydrated: 200,
dizziness: true })

/*

{
weight: Number - kilos,
experience: Number - years,
levelOfHydrated: Number - milimeters,
dizziness: Boolean
}

if dizziness is true, then that means the worker must get some water to keep working
The required amount is 0.1ml per kg per year of experience

*/

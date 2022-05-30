function CreateRegistry(strings){
  registry={}

  for(var k=0; k<strings.length;k++){
    townData=strings[k].split(" <-> ");
    if(townData[0] in registry){
      registry[townData[0]]+=Number(townData[1]);
    }else {
      registry[townData[0]]=Number(townData[1]);
    }
  }
  output=""

  for(var town in registry){
    output+=town+" : "+registry[town]+"\n";
  }
  console.log(output);
}

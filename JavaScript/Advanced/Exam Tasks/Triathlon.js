class Triathlon{
    constructor(competitionName){
        this.competitionName = competitionName;
        this.participants = {};
        this.listOfFinalists = []
    }

    addParticipant(participantName, participantGender){
        let players = Object.keys(this.participants);

        if(players.indexOf(participantName) != -1){
            return `${participantName} has already been added to the list`
        }else {
            this.participants[participantName] = participantGender;
            return `A new participant has been added - ${participantName}`;
        }
    }

    completeness(participantName, condition){
        let players = Object.keys(this.participants);

        if(players.indexOf(participantName) == -1){
            throw new Error(`${participantName} is not in the current participants list`);
        }else if(condition < 30) {
            throw new Error(`${participantName} is not well prepared and cannot finish any discipline`);
        }else {
            let completedCount = Math.floor(condition / 30);
            if(completedCount <= 2 && completedCount > 0){
                return `${participantName} could only complete ${completedCount} of the disciplines`;
            }else {
                let participantGender = this.participants[participantName];
                this.listOfFinalists.push({participantName, participantGender});
                return `Congratulations, ${participantName} finished the whole competition`;
            }
        }
    }

    rewarding(participantName){
        for(var pObj of this.listOfFinalists){
            if (pObj.participantName == participantName){
                return `${participantName} was rewarded with a trophy for his performance`;
            }
        }
        return `${participantName} is not in the current finalists list`;
    }

    showRecord(criteria){
        if(this.listOfFinalists.length == 0){
            return `There are no finalists in this competition`
        }else {
            if(criteria == "male"){

            }else if(criteria == "female"){

            }else if(criteria == "all"){
                let output = `List of all ${this.competitionName} finalists:\n`
                let allFinalists = []

                for(var pObj of this.listOfFinalists){
                    allFinalists.push(pObj.participantName);
                }
                allFinalists.sort();
                output += allFinalists.join("\n");
                return output;
            }
        }
    }
}


//Test 1
// const contest = new Triathlon("Dynamos");
// console.log(contest.addParticipant("Peter", "male"));
// console.log(contest.addParticipant("Sasha", "female"));
// console.log(contest.addParticipant("Peter", "male"));

//Test 2
// const contest = new Triathlon("Dynamos");
// console.log(contest.addParticipant("Peter", "male"));
// console.log(contest.addParticipant("Sasha", "female"));
// console.log(contest.addParticipant("George", "male"));
// console.log(contest.completeness("Peter", 100));
// console.log(contest.completeness("Sasha", 70));
// console.log(contest.completeness("George", 20));

//Test 3
// const contest = new Triathlon("Dynamos");
// console.log(contest.addParticipant("Peter", "male"));
// console.log(contest.addParticipant("Sasha", "female"));
// console.log(contest.completeness("Peter", 100));
// console.log(contest.completeness("Sasha", 70));
// console.log(contest.rewarding("Peter"));
// console.log(contest.rewarding("Sasha"));

//Test 4
// const contest = new Triathlon("Dynamos");
// console.log(contest.showRecord("all"));

//Test 5
const contest = new Triathlon("Dynamos");
console.log(contest.addParticipant("Peter", "male"));
console.log(contest.addParticipant("Sasha", "female"));
console.log(contest.completeness("Peter", 100));
console.log(contest.completeness("Sasha", 90));
console.log(contest.rewarding("Peter"));
console.log(contest.rewarding("Sasha"));
console.log(contest.showRecord("all"));
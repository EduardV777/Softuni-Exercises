window.addEventListener("load", solve);

function solve() {
  let submitButton = document.getElementById("form-btn");
  let inProgressList = document.getElementById("in-progress");
  let completedList = document.getElementById("finished");
  let firstNameF = document.getElementById("first-name");
  let lastNameF = document.getElementById("last-name");
  let ageF = document.getElementById("age");
  let genderSelect = document.getElementById("genderSelect");
  let descF = document.getElementById("task");
  let clearButton = document.getElementById("clear-btn");
  let progressCount = document.getElementById("progress-count");

  submitButton.addEventListener('click', () => {
    if(firstNameF.value.length != 0 && lastNameF.value.length != 0 && ageF.value.length != 0 && descF.value.length != 0) {
      let articleElement = document.createElement("article");
      let listRecord = document.createElement("li");
      let head4 = document.createElement("h4");
      let sexAge = document.createElement("p");
      let description = document.createElement("p");
      let editButton = document.createElement("button");
      let completeButton = document.createElement("button");


      head4.textContent = `${firstNameF.value} ${lastNameF.value}`;
      sexAge.textContent = `${genderSelect.value}, ${ageF.value}`;
      description.textContent = `Dish description: ${descF.value}`;
      editButton.textContent = "Edit";
      completeButton.textContent = "Mark as complete";
      editButton.setAttribute("class", "edit-btn");
      completeButton.setAttribute("class", "complete-btn");

      listRecord.setAttribute("class", "each-line");

      inProgressList.appendChild(listRecord);
      listRecord.appendChild(articleElement);
      articleElement.appendChild(head4);
      articleElement.appendChild(sexAge);
      articleElement.appendChild(description);
      listRecord.appendChild(editButton);
      listRecord.appendChild(completeButton);


      
      firstNameF.value = "";
      lastNameF.value = "";
      ageF.value = "";
      descF.value = "";

      let progress = Number(progressCount.textContent) + 1;
      progressCount.textContent = String(progress);
      
      editButton.addEventListener("click", () => {
        let parentContainer = articleElement;
        
        firstNameF.value = head4.textContent.split(" ")[0];
        lastNameF.value = head4.textContent.split(" ")[1];
        ageF.value = sexAge.textContent.split(", ")[1];
        genderSelect.value = sexAge.textContent.split(", ")[0];
        descF.value = description.textContent;
        inProgressList.removeChild(listRecord);

        let progress = Number(progressCount.textContent) - 1;
        progressCount.textContent = String(progress);
      });

      completeButton.addEventListener("click", () => {
        inProgressList.removeChild(listRecord);
        completedList.appendChild(listRecord);
        listRecord.removeChild(completeButton);
        listRecord.removeChild(editButton);
        let progress = Number(progressCount.textContent) - 1;
        progressCount.textContent = String(progress);
      });
    }
  });

  clearButton.addEventListener("click", () => {
    completedList.textContent = "";
  }); 
}

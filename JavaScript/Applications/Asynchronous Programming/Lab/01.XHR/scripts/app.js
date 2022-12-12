function loadRepos() {
   const request = new XMLHttpRequest();
   const url = 'https://api.github.com/users/testnakov/repos';
   
   
   request.addEventListener("readystatechange", function() {
      if(request.readyState == 4){
         const content = request.responseText;
         const container = document.getElementById("res");
         container.textContent = request.responseText;
      }
   });
   
   request.open("GET", url);
   request.send();
}
//sessionStorage.setItem("accountName", "none");
localStorage.setItem("loggedIn", "unlogged");

const homePage = document.querySelector("section#home");
const dashboardPage = document.querySelector("section#dashboard");
const registerPage = document.querySelector("section#register");
const loginPage = document.querySelector("section#login");
const createPage = document.querySelector("section#create");
const detailsPage = document.querySelector("section#details");
const editPage = document.querySelector("section#edit");
const searchPage = document.querySelector("section#search");

const pages = [dashboardPage, registerPage,loginPage, createPage, detailsPage, editPage, searchPage];

for(let p of pages){
    p.style.display = "none";
}




function navBar(){
    let sessionStatus = localStorage.getItem("loggedIn");
    let guestOptions = document.querySelector("div.guest");
    let userOptions = document.querySelector("div.user");

    let guestButtons = document.querySelectorAll("div.guest a");


    if(sessionStatus == "logged"){
      console.log("works");
      guestOptions.style.display = "none";
    }else{
        guestOptions.style.display = "span";  
        userOptions.style.display = "none";
    }

    //login button
    guestButtons[0].addEventListener("click", () => {
        homePage.style.display = "none";
        loginPage.style.display = "block";
        const loginButton = document.querySelector("section#login form button[type='submit']");

        loginButton.addEventListener("click", function(event){
            event.preventDefault();
        });

        loginButton.addEventListener("click", async function() {

            const nameField = document.querySelector("section#login input#email");
            const passwordField = document.querySelector("section#login input#password");

            const email = nameField.value;
            const password = passwordField.value;

            let res = await fetch("http://localhost:3030/user/login", {
                method: 'POST',
                headers: {
                    email,
                    password
                }
            })

            console.log(res);
        });
    });

}





navBar();
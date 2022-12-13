localStorage.setItem("loggedIn", "unlogged");

const homePage = document.querySelector("section#home");
const dashboardPage = document.querySelector("section#dashboard");
const registerPage = document.querySelector("section#register");
const loginPage = document.querySelector("section#login");
const createPage = document.querySelector("section#create");
const detailsPage = document.querySelector("section#details");
const editPage = document.querySelector("section#edit");

const pages = [dashboardPage, registerPage, loginPage, createPage, detailsPage, editPage];

function hidePages(){
    for(let p of pages){
        p.style.display = "none";
    }
}

hidePages();


const headerTexts = document.querySelectorAll("h2");

for(let h of headerTexts){
    if(h.textContent == "Products" || h.textContent == "No products yet."){
        h.style.display = "none";
    }
}


function navBar(){
    const guestOptions = document.querySelector("nav div.guest");
    const userOptions = document.querySelector("nav div.user");

    if(localStorage.getItem("loggedIn") == "logged"){
        guestOptions.style.display = "none";
        const userButtons = document.querySelectorAll("nav div.user a");

        //logout button
        userButtons[1].addEventListener("click" , Logout);

    }else {
        userOptions.style.display = "none";
        const guestButtons = document.querySelectorAll("nav div.guest a");

        //loginButton
        guestButtons[0].addEventListener("click", () => {
            homePage.style.display = "none";
            hidePages();
            loginPage.style.display = "block";

            const loginSubmitButton = document.querySelector("section#login form button");

            loginSubmitButton.addEventListener("click", (event) => { event.preventDefault()});
            loginSubmitButton.addEventListener("click", Login);
        });

        //registerButton
        guestButtons[1].addEventListener("click", () => {
            homePage.style.display = "none";
            hidePages();
            registerPage.style.display = "block";

            const registerSubmitButton = document.querySelector("section#register form button");

            registerSubmitButton.addEventListener("click", (event) => event.preventDefault());
            registerSubmitButton.addEventListener("click", Register);
        })
    }
}

async function Login(){
    const emailField = document.querySelector("section#login form input#email");
    const passwordField = document.querySelector("section#login form input#password");

    const email = emailField.value;
    const password = passwordField.value;

    if(email != "" || password != ""){
        const expectedToken = await fetch('/users/login', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        //only success case
        localStorage.setItem("accessToken", expectedToken.accessToken);
        localStorage.setItem("loggedIn", "logged");

        //redirect to products page and update navbar
        navBar()
        hidePages();
        dashboardPage.style.display = "block";
    }
}


async function Register(){
    const emailField = document.querySelector("section#register form input#register-email");
    const passwordField = document.querySelector("section#register form input#register-password");
    const repeatPasswordField = document.querySelector("section#register form input#repeat-password");

    if(emailField.value != "" || passwordField.value != "" || repeatPasswordField.value != ""){
        if(passwordField.value == repeatPasswordField.value){
            const email = emailField.value;
            const password = passwordField.value;

            let res = await fetch('/users/register',{
                method: "POST",
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({email, password})
            });

            //success case
            localStorage.setItem("accessToken", res.accessToken);
            localStorage.setItem("loggedIn", "logged");

            //redirect to products page and update navbar
            hidePages();
            dashboardPage.style.display = "block";
            navBar();
        }else {
            alert("Passwords do not match! Try again.");
        }
    }else {
        alert("Please fill out all required fields!");
    }
}

async function Logout(){
    let auth = localStorage.getItem("accessToken");

    let res = await fetch('/users/logout', {
        method: "GET",
        body: { 'X-Authorization': auth }
    })

    localStorage.setItem("loggedIn", "unlogged");
    localStorage.removeItem("accessToken");
    hidePages();
    navBar();
    dashboardPage.style.display = "block";
}

async function GetProducts(){

}

navBar();
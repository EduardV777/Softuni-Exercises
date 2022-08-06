var loggedIn = false;

var homepage = document.querySelector("section#home");
var dashboardSection = document.querySelector("section#dashboard");
var registerSection = document.querySelector("section#register");
var loginSection = document.querySelector("section#login");
var createPageSection = document.querySelector("section#create");
var detailsSection = document.querySelector("section#details");
var editSection = document.querySelector("section#edit");
var detailsSection = document.querySelector("section#details")

function checkLoginState(){
    if (loggedIn == true){
        guestOptions.style.display = "none";
        loggedInOptions.style.display = "block";
    }else {
        loggedInOptions.style.display = "none";
        guestOptions.style.display = "block";
    }
}



function HideSections(hPage = false) {
    if (hPage == false){
        homepage.style.display = "none";
    }
    dashboardSection.style.display = "none";
    registerSection.style.display = "none";
    loginSection.style.display = "none";
    createPageSection.style.display = "none";
    detailsSection.style.display = "none";
    editSection.style.display = "none";
    detailsSection.style.dispaly = "none";
}
HideSections(true);
//navbar

loggedInOptions = document.querySelector("div.user");
guestOptions = document.querySelector("div.guest");
dashboardButton = document.querySelector("a#dashBut");
loginButton = document.querySelector("a#loginBut");
registerButton = document.querySelector("a#registerBut");
logo = document.querySelector("a#logo");

logo.setAttribute("href", "#home");

checkLoginState();

dashboardButton.addEventListener("click", async () => { 
    HideSections(); 
    dashboardSection.style.display = "block";
    var offers = await fetch("http://localhost:3030/data/offers?sortBy=_createdOn%20desc");
    offers = await offers.json();
    if (offers.length != 0){
        msgOffers = document.querySelector("section#dashboard h2.no");
        msgOffers.style.display = "none";
    }
});
loginButton.addEventListener("click", () => { HideSections(); loginSection.style.display = "block" });
registerButton.addEventListener("click", () => { HideSections(); registerSection.style.display = "block" });
logo.addEventListener("click", () => { HideSections(); homepage.style.display = "block" })
//navbar

//login

emailField = document.querySelector("input#email");
passwordField = document.querySelector("input#password");
submitButton = document.querySelector("section#login div.form form.login-form button[type='submit']");

//submitButton.addEventListener("submit", preventDefault())
submitButton.addEventListener("click", async () => {
    email = emailField.value;
    password = passwordField.value;
    data = {email: `${email}`, password: `${password}`};

    if(email.length != 0 && password.length != 0 ){
        var res = await fetch("http://localhost:3030/users/login", {method: "post", headers: {"Content-Type": "application/json"}, body: JSON.stringify({email, password})});
        if(res.ok == true){
            loggedIn = true;
            res = await res.json();
            console.log(res);
            HideSections();
            checkLoginState();
            dashboardSection.style.display = "block";
            sessionStorage.setItem("userData", JSON.stringify(res));
        }
    }else {
        alert("Login data is invalid!");
    }
});

//login



//register

var registerButton = document.querySelector("section#register div.form form.login-form button[type='submit']");
var registerEmail = document.getElementById("register-email");
var registerPassword = document.getElementById("register-password");
var repeatPassword = document.getElementById("repeat-password");

registerButton.addEventListener("click", async () => {
    if(registerEmail.value.length == 0 || registerPassword.value.length == 0 || repeatPassword.value.length == 0){
        alert("Registration unsuccessful");
    }else{
        var email = registerEmail.value, password = registerPassword.value;
        var res = await fetch("http://localhost:3030/users/register", {method: "post", headers: {"Content-Type": "application/json"}, body: JSON.stringify({email, password})});
        if(res.ok == true){
            loggedIn = true;
            res = await res.json();
            HideSections();
            checkLoginState();
            dashboardSection.style.display = "block";
            sessionStorage.setItem("userData", JSON.stringify(res));
            //console.log(sessionStorage.userData);
        }
    }
});

//register


//logout
var logoutButton = document.querySelector("div.user a#logout");

logoutButton.addEventListener("click", async () => {
    var req = await fetch("http://localhost:3030/users/logout", {
        method: "get",
        headers: {'Content-Type': "text/plain", "X-Authorization": sessionStorage.userData.accessToken}
    });

    if(req.ok == true){
        req = await req.text();
        console.log(req);
        loggedIn = false;
        checkLoginState();
    }
});

//logout



//dashboard
var details1 = document.querySelector("section#dashboard div.offer a#det1");

details1.addEventListener("click", () => {HideSections(); detailsSection.style.display = "block"});

//dashboard

//create new offer
var createOfferButton = document.querySelector("div.user a#createoffer");

var titleF = document.querySelector("section#create div.form form.create-form input#job-title");
var companyLogoF = document.querySelector("section#create div.form form.create-form input#job-logo");
var jobCategoryF = document.querySelector("section#create div.form form.create-form input#job-category");
var jobDescF = document.querySelector("section#create div.form form.create-form input#job-description");
var jobReqF = document.querySelector("section#create div.form form.create-form input#job-requirements");
var salaryF = document.querySelector("section#create div.form form.create-form input#job-salary");
var postOfferButton = document.querySelector("section#create div.form form.create-form button[type='submit']")

createOfferButton.addEventListener("click", () => {
    HideSections();
    createPageSection.style.display = "block";
});

postOfferButton.addEventListener("submit", async () => { 
    if (titleF.value.length > 0 && companyLogoF.value.length > 0 && jobCategoryF.value.length > 0 && jobDescF.value.length > 0 && jobReqF.value.length > 0 && salaryF.value.length > 0){
        var createRequest = await fetch("http://localhost:3030/data/offers",{
            method: "post",
            headers: {"Content-Type": "application/json", "X-Authorization": sessionStorage.userData.accessToken},
            body: JSON.stringify({titleF, companyLogoF, jobCategoryF, jobDescF, jobReqF, salaryF})
        })
        
        if (createRequest.ok){
            createRequest = await createRequest.json();
            console.log(createRequest);
        }
    }
});



//create new offer
                                        //!!tbc!!
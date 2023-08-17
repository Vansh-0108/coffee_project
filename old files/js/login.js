let upbtn = document.getElementById("signupbtn");
let inbtn = document.getElementById("signinbtn");
let name_field = document.getElementById("name-field");
let title = document.getElementById("title");

inbtn.onclick = function(){
    name_field.style.maxHeight = "0";
    title.innerHTML = "Sign In";
    upbtn.classList.add("disable");
    inbtn.classList.remove("disable");
    // if(!inbtn.classList.contains("disable")){
        // title.innerHTML = "ehehe";
        console.log(inbtn.classList.contains("disable"));
    // }
}
upbtn.onclick = function(){
    name_field.style.maxHeight = "65px";
    title.innerHTML = "Sign Up";
    inbtn.classList.add("disable");
    upbtn.classList.remove("disable");
}

inbtn.onclick = function(){
    if(inbtn.classList.contains("disable")){
        name_field.style.maxHeight = "0";
        title.innerHTML = "Sign In";
        upbtn.classList.add("disable");
        inbtn.classList.remove("disable");
    }
    else{
            auth();
    }
}

function auth(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if(email == "admin@gmail.com" && password == "admin123"){
        window.location.assign("/index.html");
        alert("Login Successful");
    }
    else{
        alert("Invalid");
        return;
    }
}
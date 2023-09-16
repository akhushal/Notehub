var username,password;
function readfrom(){
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    password1 = document.getElementById("password1").value;
    console.log(username,password,password1);
}
function signup(){
    readfrom();
    if(password == password1){
        firebase
        .database()
        .ref("login/"+username)
        .set({
            username : username,
            password : password,
        });
        alert("insert successfully");
        document.getElementById("username").value="";
        document.getElementById("password").value="";
        document.getElementById("password1").value="";
    }
    
}
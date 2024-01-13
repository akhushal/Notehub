var username,password;
function readfrom(){
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    console.log(username,password);
}
function login(){
    readfrom();
    firebase
        .database()
        .ref("login/"+username)
        .on("value",function(snap){
            user = snap.val()
        //    console.log(user)    
                if(user.username==username){
                    if(user.password==password)
                        window.location.href=`index2.html?username=${username}`
                }
            // location.reload();
        })
}

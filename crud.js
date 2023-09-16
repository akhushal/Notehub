const urlParams = new URLSearchParams(window.location.search);
const username = urlParams.get('username');
console.log("username:",username)
document.getElementsByClassName("username").innerHTML=`${username}`;
document.getElementById('user1').innerHTML=`${username}`;
function uploadhtml(){
    window.location.href=`upload.html?username=${username}`
}
function home(){
    window.location.href=`index2.html?username=${username}`
}
function notes(){
    window.location.href=`sticky.html?username=${username}`
}
function redirectToLogin(){
    window.location.replace("index.html");
}



let subjectValue, selectedValue;
function selectCard(branch) {
    document.getElementById("semesterSelect").style.display = "block";
    var semester = document.getElementById("semesterSelect");

    semester.addEventListener("change", b);
    function b() {
        selectedValue = semester.value;
        console.log("Selected value: " + selectedValue);
        console.log("brach name: ", branch);
        if (selectedValue == "Sem6" && branch == "IT") {
            console.log("it and sem6");
            // JavaScript
            document.getElementById("itsem6").style.display = "block";
            var subject = document.getElementById("itsem6");

            subject.addEventListener("change", c);
            let x = 0;
            function c() {
                subjectValue = subject.value;
                console.log("Subject value: " + subjectValue);

                document
                    .getElementById("pdfInput")
                    .addEventListener("change", handleFileSelect, false);
                function handleFileSelect(event) {
                    const file = event.target.files[0];
                    uploadFile(file);
                }
                function uploadFile(file) {
                    let fname = document.getElementById("names").value;
                    let all = selectCard();
                    console.log(all);

                    // // Create a storage reference
                    const storageRef = firebase.storage().ref();

                    // // Generate a unique file name for the PDF
                    const fileName = `${branch}/` + `${selectedValue}/` + `${subjectValue}/` + `${fname}`;

                    // // Upload the file to Firebase Storage
                    const uploadTask = storageRef.child(fileName).put(file);

                    // Listen for state changes, errors, and completion of the upload
                    uploadTask.on(
                        "state_changed",
                        (snapshot) => {
                            // Track upload progress here if needed
                        },
                        (error) => {
                            // Handle any errors during upload
                            console.error("Error uploading the file:", error);
                        },
                        () => {
                            // Handle successful upload completion
                            console.log("File uploaded successfully!");

                            // Get the download URL of the uploaded file
                            uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
                                console.log("Download URL:", downloadURL);
                                alert(`${fname}`, " uploaded successfully")
                                // Save the download URL to Firebase Database or perform further actions
                                // ...
                                // newfile(downloadURL);
                                // const link = document.createElement('a');
                                // link.href = downloadURL;
                                // link.textContent = 'Download PDF';
                                // document.body.appendChild(link);
                                // document.getElementsByClassName('.heading').innerHTML=downloadURL;
                            });
                        }
                    );
                }

                function newfile(downloadURL) {
                    newfile(downloadURL);
                    const link = document.createElement("a");
                    link.href = downloadURL;
                    link.textContent = "Download PDF";
                    document.body.appendChild(link);
                }

                return subjectValue;
            }

            let coutput = c();
            if (coutput === "ml") console.log("coutput: ", c());
        }

        if (selectedValue == "Sem6" && branch == "ME") {
            console.log("me and sem6");
            // JavaScript
            document.getElementById("mesem6").style.display = "block";
            var subject = document.getElementById("mesem6");

            subject.addEventListener("change", c);
            let x = 0;
            function c() {
                subjectValue = subject.value;
                console.log("Subject value: " + subjectValue);

                document
                    .getElementById("pdfInput")
                    .addEventListener("change", handleFileSelect, false);
                function handleFileSelect(event) {
                    const file = event.target.files[0];
                    uploadFile(file);
                }
                function uploadFile(file) {
                    let fname = document.getElementById("names").value;
                    let all = selectCard();
                    console.log(all);

                    // // Create a storage reference
                    const storageRef = firebase.storage().ref();

                    // // Generate a unique file name for the PDF
                    const fileName = `${branch}/` + `${selectedValue}/` + `${subjectValue}/` + `${fname}`;

                    // // Upload the file to Firebase Storage
                    const uploadTask = storageRef.child(fileName).put(file);

                    // Listen for state changes, errors, and completion of the upload
                    uploadTask.on(
                        "state_changed",
                        (snapshot) => {
                            // Track upload progress here if needed
                        },
                        (error) => {
                            // Handle any errors during upload
                            console.error("Error uploading the file:", error);
                        },
                        () => {
                            // Handle successful upload completion
                            console.log("File uploaded successfully!");

                            // Get the download URL of the uploaded file
                            uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
                                console.log("Download URL:", downloadURL);
                                alert(`${fname}`, " uploaded successfully")
                                // Save the download URL to Firebase Database or perform further actions
                                // ...
                                // newfile(downloadURL);
                                // const link = document.createElement('a');
                                // link.href = downloadURL;
                                // link.textContent = 'Download PDF';
                                // document.body.appendChild(link);
                                // document.getElementsByClassName('.heading').innerHTML=downloadURL;
                            });
                        }
                    );
                }

                function newfile(downloadURL) {
                    newfile(downloadURL);
                    const link = document.createElement("a");
                    link.href = downloadURL;
                    link.textContent = "Download PDF";
                    document.body.appendChild(link);
                }

                return subjectValue;
            }

            let coutput = c();
            if (coutput === "ml") console.log("coutput: ", c());
        }
        
    
    }

    return branch;
}
// JavaScript

// function answer() {
//     let branch = selectCard();
//     let
// }






function selectCardM(branch) {
    document.getElementById("semesterSelect").style.display = "block";
    let Branch = branch;
    console.log(Branch)
    var semester = document.getElementById("semesterSelect");
    semester.addEventListener("change", b);
    function b() {
        selectedValue = semester.value;
        console.log("Selected value: " + selectedValue);
        console.log("brach name: ", branch);
        if (selectedValue == "Sem6" && branch == "IT") {
            console.log("it and sem6");
            // JavaScript
            document.getElementById("itsem6").style.display = "block";
            var subject = document.getElementById("itsem6");

            subject.addEventListener("change", c);
            function c() {
                subjectValue = subject.value;
                console.log("Subject value: " + subjectValue);
                let all = `${branch}/` + `${selectedValue}/` + `${subjectValue}/`
                // sessionStorage.setItem('All: ', all);
                window.location.href = `show.html?all=${all}&branch=${branch}&sem=${selectedValue}&sub=${subjectValue}&username=${username}`
            }
        }
        if (selectedValue == "Sem6" && branch == "ME") {
            console.log("me and sem6");
            // JavaScript
            document.getElementById("mesem6").style.display = "block";
            var subject = document.getElementById("mesem6");

            subject.addEventListener("change", c);
            function c() {
                subjectValue = subject.value;
                console.log("Subject value: " + subjectValue);
                let all = `${branch}/` + `${selectedValue}/` + `${subjectValue}/`
                // sessionStorage.setItem('All: ', all);
                window.location.href = `show.html?all=${all}&branch=${branch}&sem=${selectedValue}&sub=${subjectValue}&username=${username}`
            }
        }

        return branch;
    }
}



function show() {

    const storage = firebase.storage();
    let ans = `${Branch}/` + `${selectedValue}/` + `${subjectValue}/`
    console.log(ans);
    const folderRef = storage.ref().child(`${ans}`);
    folderRef.listAll()
        .then((res) => {
            const pdfContainer = document.getElementById('pdfContainer');
            res.items.forEach((item) => {
                item.getDownloadURL()
                    .then((url) => {
                        const link = document.createElement('a');
                        link.id = 'pdf';
                        link.href = url;
                        link.target = '_blank';
                        link.textContent = item.name;
                        pdfContainer.appendChild(link);
                    })
                    .catch((error) => {
                        console.error('Error getting PDF URL:', error);
                    });
            });
        })
        .catch((error) => {
            console.error('Error listing items in the folder:', error);
        });


}


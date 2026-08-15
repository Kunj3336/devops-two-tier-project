const userForm = document.getElementById("userForm");
const statusMessage = document.getElementById("statusMessage");

userForm.addEventListener("submit", function (event) {
    event.preventDefault();

    statusMessage.style.display = "block";

    userForm.reset();
});
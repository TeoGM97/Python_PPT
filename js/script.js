//Jump class will be created and will be added and removed every time I need it
const dino = document.getElementById("dino");

function jump () {
    if (dino.classList != "jump") {
        dino.classList.add("jump");

        setTimeout(function () {
            dino.classList.remove("jump");
        }, 300);
    }
}

//Listener for key press action
document.addEventListener("keydown", function (event) {
    jump();
});
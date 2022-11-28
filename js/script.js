//Jump class will be created and will be added and removed every time I need it
const dino = document.getElementById("dino");
const cactus = document.getElementById("cactus");

function jump () {
    if (dino.classList != "jump") {
        dino.classList.add("jump");

        setTimeout(function () {
            dino.classList.remove("jump");
        }, 300);
    }
}

let isAlive = setInterval(function (){
    //get current dino Y position
    let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"));

    //get current cactus X position
    let cactusLeft = parseInt(
        window.getComputedStyle(cactus).getPropertyValue("left")
    );

    //Detect collision
    if (cactusLeft <50 && cactusLeft > 0 && dinoTop >= 140) {
    //Collision
        alert("GAME OVER");
    }
}, 10);

//Listener for key press action
document.addEventListener("keydown", function (event) {
    jump();
});
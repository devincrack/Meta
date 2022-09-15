
hrt = document.getElementById("hrt");
hrt.addEventListener("click",function () {
    if (hrt.style.color=="red") {
        hrt.style.color="grey";
    }else {
        hrt.style.color="red";
    }
})

var loader = document.getElementById("preloader");

let post = document.getElementsByClassName("post-container");

window.addEventListener("load",function () {
    loader.style.display="none"
})

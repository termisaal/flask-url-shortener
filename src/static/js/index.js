function changeTheme() {
    let dayNightButton = document.getElementById("day-night-button");
    let commonTexts = document.getElementsByClassName("common-text");

    dayNightButton.style.fontSize = "32px";
    dayNightButton.style.right = "12px";
    dayNightButton.style.bottom = "12px";
    setTimeout(() => {
        dayNightButton.style.fontSize = "24px";
        dayNightButton.style.right = "16px";
        dayNightButton.style.bottom = "16px";
    }, 250);

    if (dayNightButton.innerText === "🌑") {
        dayNightButton.innerText = "☀️";
        document.body.style.backgroundColor = "white";
        for (let commonText of commonTexts) {
            commonText.style.color = "black";
        }
    } else {
        dayNightButton.innerText = "🌑";
        document.body.style.backgroundColor = "black";
        for (let commonText of commonTexts) {
            commonText.style.color = "white";
        }
    }
}

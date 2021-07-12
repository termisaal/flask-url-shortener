function changeTheme() {
    let dayNightButton = document.getElementById("day-night-button");

    dayNightButton.style.fontSize = "32px";
    dayNightButton.style.right = dayNightButton.style.bottom = "12px";
    setTimeout(() => {
        dayNightButton.style.fontSize = "24px";
        dayNightButton.style.right = dayNightButton.style.bottom = "16px";
    }, 250);

    if (dayNightButton.innerText === "🌑") {
        dayNightButton.innerText = "☀️";
        document.cookie = "theme=light";
        console.log(document.cookie);
        document.body.setAttribute("theme", "light");
    } else {
        dayNightButton.innerText = "🌑";
        document.cookie = "theme=dark";
        console.log(document.cookie);
        document.body.setAttribute("theme", "dark");
    }
}

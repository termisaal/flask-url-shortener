function onLoad() {
    document.body.setAttribute('theme', 'dark')
}


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
        document.body.setAttribute('theme', 'light');
    } else {
        dayNightButton.innerText = "🌑";
        document.body.setAttribute('theme', 'dark');
    }
}

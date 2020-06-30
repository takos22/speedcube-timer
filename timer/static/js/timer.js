var started,reseted, stoped, start, now, time;
started = false;
reseted = false;
stoped = true;

function updateTimer() {
    if (started) {
        document.querySelector("#time").innerHTML = ((Date.now() - start) / 1000).toFixed(3);
    }
    window.requestAnimationFrame(updateTimer);
}

document.addEventListener("keyup", (event) => {
    if (event.keyCode === 32) {
        if (!started && stoped) {
            start = Date.now();
            started = true;
        } else {
            stoped = true;
            reseted = false;
        }
    }
});
document.addEventListener("keydown", (event) => {
    if (event.keyCode === 32) {
        if (!started && !reseted) {
            document.querySelector("#time").innerHTML = "0.000";
            reseted = true;
        } else if (started) {
            time = ((Date.now() - start) / 1000).toFixed(3);
            document.querySelector("#time").innerHTML = time;
            started = false;
            stoped = false;
        }
    }
});

window.requestAnimationFrame(updateTimer);

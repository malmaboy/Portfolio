var time;

function clockTime(){
    let date = new Date();
    time.innerHTML = date.toLocaleTimeString("it-IT",
        {timeZone:"Portugal"});
}

window.addEventListener("load", () => {
    time = document.getElementById("hour");
    setInterval(clockTime,1000);
})
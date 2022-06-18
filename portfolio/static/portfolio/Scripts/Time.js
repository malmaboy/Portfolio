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


let splitTitle = window.location.pathname.split("/").at(-1).split("-");
let title = "";

splitTitle.forEach((s) => {
  if (s.length > 0) {
    s = s[0].toUpperCase() + s.substring(1);
    title += s + " ";
  }
});

document.title = title === "" ? "Home" : title;



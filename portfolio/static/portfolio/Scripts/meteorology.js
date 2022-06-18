window.addEventListener("load", () => {
  fetch(
    "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
  )
    .then((response) => response.json())
    .then((data) => {
      let meteorologyEl = document.getElementById("meter");

      for (const day of data.data) {
        let dayDivEl = document.createElement("div");
        dayDivEl.classList.add("meter");

        let precipitaProbEl = document.createElement("p");
        let tMinEl = document.createElement("p");
        let tMaxEl = document.createElement("p");
        let predWindDirEl = document.createElement("p");
        let forecastDateEl = document.createElement("h2");

        dayDivEl.appendChild(forecastDateEl);
        dayDivEl.appendChild(tMinEl);
        dayDivEl.appendChild(tMaxEl);
        dayDivEl.appendChild(precipitaProbEl);
        dayDivEl.appendChild(predWindDirEl);

        let forecastDateString = day.forecastDate
          .split("-")
          .reverse()
          .join("-");

        forecastDateEl.innerHTML = forecastDateString;
        tMinEl.innerHTML = `Minimum Temperature: ${day.tMin}`;
        tMaxEl.innerHTML = `Maximum Temperature: ${day.tMax}`;
        precipitaProbEl.innerHTML = `Precipitation: ${day.precipitaProb}`;
        predWindDirEl.innerHTML = `Wind Prediction: ${day.predWindDir}`;

        meteorologyEl.appendChild(dayDivEl);
      }
    });
});
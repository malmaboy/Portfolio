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

  fetch("https://api.github.com/users/malmaboy/repos")
    .then((response) => response.json())
    .then((data) => {
      data = data.sort((r) => r.updated_at);

      let githubRepos = document.getElementById("git");

      for (const repo of data) {
        let repoAnchorEl = document.createElement("a");

        let githubRepoEl = document.createElement("div");
        githubRepoEl.classList.add("github");

        let repoNameEl = document.createElement("h2");
        let descriptionEl = document.createElement("p");
        let languageEl = document.createElement("p");
        let createdAtEl = document.createElement("h4");

        repoAnchorEl.appendChild(githubRepoEl);

        githubRepoEl.appendChild(repoNameEl);
        githubRepoEl.appendChild(descriptionEl);
        githubRepoEl.appendChild(languageEl);
        githubRepoEl.appendChild(createdAtEl);

        repoAnchorEl.href = repo.html_url;
        repoAnchorEl.setAttribute("target", "_blank");

        let creationYear = repo.created_at.split("-")[0];

        repoNameEl.innerHTML = repo.name;
        descriptionEl.innerHTML = repo.description;
        languageEl.innerHTML = `Language: ${repo.language}`;
        createdAtEl.innerHTML = creationYear;

        githubRepos.appendChild(repoAnchorEl);
      }
    });


});
'use strict';

const queryForm = document.querySelector('#search-form');
const resultsContainer = document.querySelector('#results');

queryForm.addEventListener('submit', async function(event) {
  event.preventDefault();

  const queryInput = document.querySelector('#query');
  const query = queryInput.value;

  try {

    resultsContainer.innerHTML = '';

    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`,
    );
    const results = await response.json();

    results.forEach((tvShow) => {
      const show = tvShow.show;

      const article = document.createElement('article');

      const nameElement = document.createElement('h2');
      nameElement.textContent = show.name;
      article.appendChild(nameElement);

      const linkElement = document.createElement('a');
      linkElement.href = show.url;
      linkElement.textContent = 'Lisätiedot';
      linkElement.target = '_blank';
      article.appendChild(linkElement);

      const imageElement = document.createElement('img');
      imageElement.src = show.image ? show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
      imageElement.alt = show.name;
      article.appendChild(imageElement);

      if (show.summary) {
        const summaryElement = document.createElement('div');
        summaryElement.innerHTML = show.summary;
        article.appendChild(summaryElement);
      }

      resultsContainer.appendChild(article);
    });
  } catch (error) {
    console.log('Virhe latauksessa:', error.message);
  }
});

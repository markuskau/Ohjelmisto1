'use strict';

const queryForm = document.querySelector('#search-form');

queryForm.addEventListener('submit', async function(event) {
  event.preventDefault();

  const queryInput = document.querySelector('#query');
  const query = queryInput.value;

  try {
    const response = await fetch(
        `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`,
    );

    const results = await response.json();

    console.log('Hakutulokset:', results);
  } catch (error) {
    console.log('Virhe latauksessa:', error.message);
  }
});

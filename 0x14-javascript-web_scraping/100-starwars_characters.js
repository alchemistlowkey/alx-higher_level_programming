#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

request(url + movieId, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    data.characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});

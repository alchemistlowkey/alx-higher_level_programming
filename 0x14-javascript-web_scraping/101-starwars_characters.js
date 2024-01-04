#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

request(url + movieId, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printData(characters, 0);
  }
});

function printData (characters, index) {
  request(characters[index], (charError, charResponse, charBody) => {
    if (charError) {
      console.error(charError);
    } else {
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      if (index + 1 < characters.length) {
        printData(characters, index + 1);
      }
    }
  });
}

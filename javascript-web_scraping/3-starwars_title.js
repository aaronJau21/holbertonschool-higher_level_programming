#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

if (args.length < 1) {
  console.log('Por favor proporcione el ID de la película como argumento');
  process.exit(1);
}

const movieId = args[0];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function(error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: API devolvió el código de estado ${response.statusCode}`);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  console.log(`${movieData.title}`);
});

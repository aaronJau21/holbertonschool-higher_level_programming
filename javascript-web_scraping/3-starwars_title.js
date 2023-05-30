#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else if (error) {
    console.error(error);
  } else {
    console.error('Usage: ./3-starwars_title.js [movie number]');
  }
});

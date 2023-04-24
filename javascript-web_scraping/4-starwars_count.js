#!/usr/bin/node

const apiUrl = process.argv[2];
const charToSearch = 18;
const request = require('request');

request.get(apiUrl, (error, response, body) => {
    if (error) console.log(error);
    let films = JSON.parse(body).results;
    films = films.filter(
        film => film.characters.find(
            character => character.match(charToSearch)
        )
    );
    console.log(films.length);
});
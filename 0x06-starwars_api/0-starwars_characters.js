#!/usr/bin/node

const request = require('request');

// Request URL
const url = 'https://swapi-api.alx-tools.com/api/films/${movieId}/';

request(url, (error, response, body) => {
    // Printing the error if occurred
    if (error) console.log(error)

    // Printing status code
    console.log(response.statusCode);

    // Printing body
    console.log(body);
});

#!/usr/bin/node

const request = require('request');
const starWarId = 'https://swapi-api.hbtn.io/api/films/:id'.concat(process.argv[2]);

request(starWarId, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});

#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/:id' + process.argv[2];

request({ url: url, json: true }, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log(res.body.title);
  }
});

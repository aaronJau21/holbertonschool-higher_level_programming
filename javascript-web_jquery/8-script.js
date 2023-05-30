/* .getJSON() retrieve JSON data and automatically parses the returned JSON data*/
$(document).ready(function () {
  $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (i, movie) {
      $('<li>').text(movie.title).appendTo('ul#list_movies');
    });
  });
});

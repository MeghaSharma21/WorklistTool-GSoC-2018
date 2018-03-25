/**
 * Function that fetches the articles corresponding to a petscan query id .
 *
 * 'encodeURIComponent' function has been used to escape unsafe characters in the URL.
 * Similarly, unsafe characters have been escaped in HTML also.
 * This will prevent injection in HTML and URL.
 */
function fetchArticles() {
  //Displaying 'Fetching Results' message till the actual results get loaded.
  document.getElementById("results").innerHTML =
    "<div class='panel panel-default message'> " +
    "<div class='panel-body'>Fetching Results....</div></div>";
  var searchTerm = document.getElementById('search').value;
  var url = "https://tools.wmflabs.org/gsoc-petscan-query-articles" +
    "/get-petscan-query-articles/";
  //Ajax call that sends the query to fetch articles corresponding
  // to a petscan query id
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    data: {
      psid: searchTerm,
    },
    success: function(data, status, jqXHR) {
      var html = "";
      if (!data.result) {
        $('#results').empty();
        alert(data.message);
        html = "<div class='panel panel-default message'> " +
          "<div class='panel-body'>No articles!</div></div>";
        $('#results').html(html);
      } else {
        articles = data.articles;
        var articleLink, articleSize, articleSizeNumberAndUnit,
          articleSizeNumber, articleSizeUnit, date;
        for (var i = 0; i < articles.length; i++) {
          articleLink =
            "<a class='stat-value' href ='https://en.wikipedia.org/wiki/" +
            encodeURIComponent(articles[i].title.replace(/ /g, "_")) +
            "'><i class='fa fa-pencil-square-o fa-edit-icon' aria-hidden='true'></i></a>";
          articleSize = formatBytes(articles[i].len);
          articleSizeNumberAndUnit = articleSize.split(" ");
          articleSizeNumber = articleSizeNumberAndUnit[0];
          articleSizeUnit = articleSizeNumberAndUnit[1];
          date = getDate(String(articles[i].touched));
          html +=
            "<div class='wrapper inline'>" +
            "<div class='info-card pink'>" +
            "<div class='info-card__level info-card__level--pink'>" +
            date + "</div>" +
            "<div class='info-card__unit-name'>" + articles[i].title
            .replace(/</g, "&lt;").replace(/>/g, "&gt;") + "</div>" +
            "<div class='info-card__unit-description'>" +
            "<strong>NameSpace Text: </strong>" + articles[i].nstext +
            "</div>" +
            "<div class='info-card__unit-stats info-card__unit-stats--pink clearfix'>" +
            "<div class='one-third'>" +
            "<div class='stat'>" + articleLink + "</div>" +
            "<div class='stat-value fa-icon-name'>Article</div>" +
            "</div>" +
            "<div class='one-third'>" +
            "<div class='stat'>" + articleSizeNumber +
            "<sup>" + articleSizeUnit + "</sup>" + "</div>" +
            "<div class='stat-value'>Article Size</div>" +
            "</div>" +
            "<div class='one-third'>" +
            "<div class='stat article-id-stat'>" + articles[i].id +
            "</div>" +
            "<div class='stat-value article-id-stat-value'>Article Id</div>" +
            "</div>" +
            "</div>" +
            "</div>" +
            "</div>";
        }
        //Handling the case when there are no edits by the specified user.
        if (articles.length == 0) {
          html = "<div class='panel panel-default message' >" +
            "<div class='panel-body'> No articles in PetScan Query ID " +
            searchTerm.replace(/</g, "&lt;").replace(/>/g, "&gt;") +
            "</div></div>";
        }
        $('#results').html(html);
      }
    },
    error: function(jqXHR, textStatus, error) {
      $('#results').empty();
      formatAjaxErrorMessage(jqXHR, error);
      var html = "<div class='panel panel-default message'> " +
        "<div class='panel-body'>No results!</div></div>";
      $('#results').html(html);
    }
  });
}

/**
 * Function to handle errors being thrown from an ajax call
 */
function formatAjaxErrorMessage(jqXHR, error) {
  switch (jqXHR.status) {
    case 0:
      alert("Verify your network. No connection!");
      return;

    case 500:
      alert("500 - Internal Server Error.");
      return;

    case 404:
      alert("404 - Requested page cannot be found");
      return;

    default:
      alert("Error:\n" + jqXHR.responseText);
  }
}

/*
 * Function to Convert size in bytes to KB, MB, GB etc
 */
function formatBytes(bytes, decimals) {
  if (bytes == 0) return '0 Bytes';
  var k = 1024,
    dm = decimals || 1,
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

/*
 * Function to convert timestamp string to date
 */
function getDate(timestamp) {
  var year = timestamp.slice(0, 4),
    month = timestamp.slice(4, 6),
    day = timestamp.slice(6, 8),
    hours = timestamp.slice(8, 10),
    minutes = timestamp.slice(10, 12),
    seconds = timestamp.slice(12, 14);
  var date = new Date(year, parseInt(month) - 1, day, hours, minutes, seconds);
  return date;
}

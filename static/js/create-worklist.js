// logic for adding new article box on button click
var noOfArticles = 0;
function addNewArticle() {
    noOfArticles++;
    var html = '<div id="article-'+noOfArticles+'"><br/><h3>Article '
        + noOfArticles +'</h3>Name of Article: <input style="width: 572px;" type="text" ' +
        'class="article-name" name="article-name" placeholder="Enter name of the article">' +
        '<br/>Description: <input style="width: 600px;" type="text" name="article-description" ' +
        'class="article-description" placeholder="Enter description of the work to be done ' +
        'for this article"><br/>Effort: <input style="width: 644px;" type="text" ' +
        'name="article-effort" class="article-effort" placeholder="Enter estimated effort ' +
        'to do work for this article"></div>'

    $('#articles-input').append(html);
}

function saveWorklist() {
    var articlesArray = [];

    for(var i=1; i<=noOfArticles; i++)
    {
        var article = {
            'name': $('#article-'+i+' .article-name').val(),
            'effort': $('#article-'+i+' .article-effort').val(),
            'description': $('#article-'+i+' .article-description').val(),
            'created_by': $('#worklist-username').val()
        };
        articlesArray.push(article);
    }

    $.ajax({
        url: "/worklist-tool/create-worklist",
        type: "post",
        data: {
            name: $('#worklist-name').val(),
            tags: $('#worklist-tags').val(),
            description: $('#worklist-description').val(),
            created_by: $('#worklist-username').val(),
            psid: $('#worklist-psid').val(),
            articles: JSON.stringify(articlesArray),
        },
        success: function (data) {
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'>" +
                "<a href='#' class='close' data-dismiss='alert'>&times;</a> "
                + data.message + "</div>"
            );
            if(data.error == 0) {
                window.location.href = '/worklist-tool/show-tasks?worklist_name='
                + data.name + '&worklist_created_by=' + data.created_by
            }
        },
        error: function () {
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'><a href='#' " +
                "class='close' data-dismiss='alert'>&times;</a> " +
                "<strong>Oh snap! </strong>Something went wrong while" +
                " saving worklist. Please report Megha " +
                "at meghasharma4910@gmail.com</div>"
            );
        }
    });
    return false;
}

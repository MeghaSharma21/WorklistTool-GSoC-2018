// logic for adding new article box on button click
var noOfArticles = 0;
function addNewArticle() {
    noOfArticles++;
    var html = '<div id="article_'+noOfArticles+'"><br/><h3>Article '
        + noOfArticles +'</h3>Name of Article: <input type="text" ' +
        'class="article-name" name="article-name" placeholder="Enter name of the article">' +
        '<br/>Description: <input type="text" name="article-description" ' +
        'class="article-description" placeholder="Enter description of the work to be done ' +
        'for this article"><br/>Effort: <input type="text" ' +
        'name="article-effort" class="article-effort" placeholder="Enter estimated effort ' +
        'to do work for this article"></div>'

    $('#articles_input').append(html);
}

function load() {
    $('#submit_btn').html("<i class='fa fa-spinner fa-spin '></i> Creating Worklist");
    $(this).attr('disabled',true);
}

function saveWorklist() {
    var articlesArray = [];

    for(var i=1; i<=noOfArticles; i++)
    {
        var article = {
            'name': $('#article_'+i+' .article_name').val(),
            'effort': $('#article_'+i+' .article_effort').val(),
            'description': $('#article_'+i+' .article_description').val(),
            'created_by': $('#worklist_username').val()
        };
        articlesArray.push(article);
    }

    $.ajax({
        url: "/worklist-tool/create-worklist",
        type: "post",
        data: {
            name: $('#worklist_name').val(),
            tags: $('#worklist_tags').val(),
            description: $('#worklist_description').val(),
            created_by: $('#worklist_username').val(),
            psid: $('#worklist_psid').val(),
            articles: JSON.stringify(articlesArray),
        },
        success: function (data) {
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'>" +
                "<a href='#' class='close' data-dismiss='alert'>&times;</a> "
                + data.message + "</div>"
            );
            if(data.error == 0) {
                window.location.href = '/worklist-tool/show-tasks?'
                    + encodeURIComponent(worklist_created_by) + '/'
                    + encodeURIComponent(worklist_name)
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
        },
        complete: function () {
                $('#submit_btn').html("Submit");
                $(this).attr('disabled',false);
        }
    });
    return false;
}

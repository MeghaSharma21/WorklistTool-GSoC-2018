var tasks;
var worklist_name;
var worklist_created_by;
var input;
var pageState;

function saveTask(article_name, task_id, logged_in_user) {
    var status_id = "#select-status-" + task_id;
    var progress_id = "#select-progress-" + task_id;
    $.ajax({url: "/worklist-tool/update-task-info/",
        type: "post",
        data: {
            'worklist_name': worklist_name,
            'worklist_created_by': worklist_created_by,
            'article_name': article_name,
            'status': $(status_id).val(),
            'progress': $(progress_id).val(),
            'claimed_by': logged_in_user
        },
        success: function (data) {
            window.location.reload(true);
        },
        error: function () {
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'><a href='#' class='close' " +
                "data-dismiss='alert'>&times;</a> " +
                "<strong>Oh snap!</strong>Something went wrong while" +
                " saving updated information! Please report Megha " +
                "at meghasharma4910@gmail.com</div>"
            );
    }});
}

function rememberState() {
        // Finding how many rows are being displayed so that we can make it same after refresh
        var rowsPerPageDropdownIndex = $('.page-list .dropdown-menu .dropdown-item.active').index();

        // Finding which page is active so that we can make it active again after refresh
        var rowsPerPageIndex = $('.pagination .page-item.active').index();

        // Finding on which column the table is sorted
        var sortableColumns = $('.th-inner.sortable.both');
        var nameSortClass = '';
        var progressSortClass = '';
        var effortSortClass = '';
        if (sortableColumns[0].innerText == 'Name') {
            if(sortableColumns[0].classList.contains('asc')) {
                nameSortClass = 'asc';
            }
            if(sortableColumns[0].classList.contains('desc')) {
                nameSortClass = 'desc';
            }
        }
        if (sortableColumns[1].innerText == 'Progress') {
            if(sortableColumns[1].classList.contains('asc')) {
                progressSortClass = 'asc';
            }
            if(sortableColumns[1].classList.contains('desc')) {
                progressSortClass = 'desc';
            }
        }
        if (sortableColumns[2].innerText == 'Effort') {
            if(sortableColumns[2].classList.contains('asc')) {
                effortSortClass = 'asc';
            }
            if(sortableColumns[2].classList.contains('desc')) {
                effortSortClass = 'desc';
            }
        }

        return {'rowsPerPageDropdownIndex': rowsPerPageDropdownIndex,
                'rowsPerPageIndex': rowsPerPageIndex,
                'nameSortClass': nameSortClass,
                'progressSortClass': progressSortClass,
                'effortSortClass': effortSortClass
        }

}

function restoreState() {
        // making the number of rows to be same
        var dropdownElements = $('.page-list .dropdown-menu .dropdown-item');
        dropdownElements[pageState.rowsPerPageDropdownIndex].click();

        // making the same page active as was before
        var paginationElements = $('.pagination .page-item .page-link');
        paginationElements[pageState.rowsPerPageIndex].click();

        // sorting the columns as they were before
        var sortableColumns = $('.th-inner.sortable.both');
        if (sortableColumns[0].innerText == 'Name') {
            if(pageState.nameSortClass == 'asc') {
                sortableColumns[0].click();
            }
            if(pageState.nameSortClass == 'desc') {
                sortableColumns[0].click();
                sortableColumns[0].click();
            }
        }
        if (sortableColumns[1].innerText == 'Progress') {
            if(pageState.progressSortClass == 'asc') {
                sortableColumns[1].click();
            }
            if(pageState.progressSortClass == 'desc') {
                sortableColumns[1].click();
                sortableColumns[1].click();
            }
        }
        if (sortableColumns[2].innerText == 'Effort') {
            if(pageState.effortSortClass == 'asc') {
                sortableColumns[2].click();
            }
            if(pageState.effortSortClass == 'desc') {
                sortableColumns[2].click();
                sortableColumns[2].click();
            }
        }
}


function refresh() {
    search_term = $("#search_by_task_name_form input[name=search_term]").val();
    worklist_name = $("#search_by_task_name_form input[name=worklist_name]").val();
    worklist_created_by = $("#search_by_task_name_form input[name=worklist_created_by]").val();

    pageState = rememberState();

    $('#task_table').load(
        "/worklist-tool/update-task-table/" + encodeURIComponent(worklist_created_by) + "/" + encodeURIComponent(worklist_name) + "?search_term=" + encodeURIComponent(search_term), function(){
            $('#task_table').hide();
            setTimeout(function(){$('#task_table').fadeIn('slow');},0);
        });
}

function worker() {
    refresh();
    setTimeout(worker, 50000);
}

function addArticle(worklist_name, worklist_created_by) {
    $.ajax({
        url: "/worklist-tool/add-articles-to-worklistt",
        type: "post",
        data: {
            article_name: $('#article_name').val(),
            article_description: $('#article_description').val(),
            article_effort: $('#article_effort').val(),
            worklist_created_by: worklist_created_by,
            worklist_name: worklist_name
        },
        success: function (data) {
            $("#add_articles_modal").modal("hide")
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'>" +
                "<a href='#' class='close' data-dismiss='alert'>&times;</a> "
                + data.message + "</div>"
            );
            if (data.error == 0) {
                refresh();
            }
        },
        error: function () {
            $("#alert-message-holder").html(
                "<div class='alert alert-danger' role='alert'><a href='#' class='close' " +
                "data-dismiss='alert'>&times;</a> " +
                "<strong>Oh snap!</strong>Something went wrong while" +
                " saving updated information! Please report at " +
                "https://github.com/MeghaSharma21/WorklistTool-GSoC-2018/issues</div>"
            );
    }});

    return false;
}

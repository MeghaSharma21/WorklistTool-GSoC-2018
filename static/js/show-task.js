var tasks;
var worklist_name;
var worklist_created_by;

function populateModal(task) {
    $('#exampleModalLongTitle').html(task.article_name);
    $('#task-progress').val(task.progress);
    $('input:radio[name=status][value='+task.status +']').prop("checked",true);
}

function taskForm(taskIndex){
    var task = tasks[taskIndex];
    populateModal(task);
    $('#exampleModalCenter').modal();
}

function saveTask() {
    $.ajax({url: "/worklist-tool/update-task-info",
        type: "post",
        data: {
            'worklist_name': worklist_name,
            'worklist_created_by': worklist_created_by,
            'article_name': $('#exampleModalLongTitle').html(),
            'status': $('input:radio[name=status]:checked').val(),
            'progress': $('#task-progress').val(),
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

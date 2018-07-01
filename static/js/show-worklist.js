function search_by_worklist_name() {
    $('#search_by_worklist_name').removeClass('hidden');
    $('#search_by_username').addClass('hidden');
    $('#dropdownMenuButton').html('By Worklist Name');
}

function search_by_username() {
    $('#search_by_worklist_name').addClass('hidden');
    $('#search_by_username').removeClass('hidden');
    $('#dropdownMenuButton').html('By Username');
}

function refresh() {
    if($('#search_by_worklist_name').is(":visible") == true) {
        search_term = document.getElementById("search_by_worklist_name_form").search_term.value
        search_type = document.getElementById("search_by_worklist_name_form").search_type.value
    } else {
        search_term = document.getElementById("search_by_username_form").search_term.value
        search_type = document.getElementById("search_by_username_form").search_type.value
    }

    $('#worklist_table').html('');
    $('#worklist_table').addClass('loader');
    $('#worklist_table').html('').load("/worklist-tool/update-worklist-table?search_term=" +
        encodeURIComponent(search_term) + "&search_type=" + encodeURIComponent(search_type),
    function() {
      $('#worklist_table').removeClass('loader');
    }
    );
}

function worker() {
    refresh();
    setTimeout(worker, 50000);
}

$(window).on('load', function(){
    setTimeout(worker, 50000);
});

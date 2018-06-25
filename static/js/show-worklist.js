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

(window).on('load', function worker() {
     if($('#search_by_worklist_name').is(":visible") == true) {
                search_term = document.getElementById("search_by_worklist_name_form").search_term.value
                search_type = document.getElementById("search_by_worklist_name_form").search_type.value
            } else {
                search_term = document.getElementById("search_by_username_form").search_term.value
                search_type = document.getElementById("search_by_username_form").search_type.value
            }

            $('#worklist-table').html('');
            $('#worklist-table').addClass('loader');
            $('#worklist-table').html('').load(
            "/worklist-tool/update-worklist-table?search_term=" + search_term + "&search_type=" + search_type,
            function() {
              $('#worklist-table').removeClass('loader');
            }
            );

            setTimeout(worker, 50000);
});

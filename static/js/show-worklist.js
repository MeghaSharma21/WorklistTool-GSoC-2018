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
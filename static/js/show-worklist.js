var worklists = [];
var awesomplete_by_worklist_name;
var awesomplete_by_username;

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

function rememberState() {
	// Finding how many number of rows are being displayed so that we can make it same after refresh
        var dropdownElements = $('.page-list .dropdown-menu .dropdown-item');
        var activeDropdownElement = $('.page-list .dropdown-menu .dropdown-item.active')[0];
        for(var i=0; i < dropdownElements.length; i++)
        {
            if (dropdownElements[i] === activeDropdownElement) {
                activeDropdownElementIndex = i;
            }
        }

        // Finding which page is active so that we can make it active again after refresh
        var paginationElements = $('.pagination .page-item .page-link');
        var activeElement = $('.pagination .page-item.active .page-link')[0];
        for(var i=0; i < paginationElements.length; i++)
        {
            if (paginationElements[i] === activeElement) {
                activeElementIndex = i;
            }
        }
}

function restoreState() {
      // making the number of rows to be same
      var dropdownElements = $('.page-list .dropdown-menu .dropdown-item');
      dropdownElements[activeDropdownElementIndex].click();

      // making the same page active as was before
      var paginationElements = $('.pagination .page-item .page-link');
      paginationElements[activeElementIndex].click();
}

function refresh() {
    if($('#search_by_worklist_name').is(":visible") == true) {
        search_term = $("#search_by_worklist_name_form input[name=search_term]").val();
        search_type = $("#search_by_worklist_name_form input[name=search_type]").val();
    } else {
        search_term = $("#search_by_username_form input[name=search_term]").val();
        search_type = $("#search_by_username_form input[name=search_type]").val();
    }

    rememberState();

    $('#worklist_table').html('');
    $('#worklist_table').addClass('loader');
    $('#worklist_table').html('').load("/worklist-tool/update-worklist-table?search_term=" +
        encodeURIComponent(search_term) + "&search_type=" + encodeURIComponent(search_type),
    function() {
      $('#worklist_table').removeClass('loader');
    }
    );

    setTimeout(restoreState, 2000);

}

function worker() {
    refresh();
    setTimeout(worker, 50000);
}

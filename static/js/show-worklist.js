var worklists = [];
var awesomplete_by_worklist_name;
var awesomplete_by_username;
var rowsPerPageIndices;
var pageState;

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
    // Finding how many rows are being displayed so that we can make it same after refresh
    var rowsPerPageDropdownIndex = $('.page-list .dropdown-menu .dropdown-item.active').index();

    // Finding which page is active so that we can make it active again after refresh
    var rowsPerPageIndex = $('.pagination .page-item.active').index();

    // Remember the state of the column on which the table is sorted
    var sortableColumns = $('.th-inner.sortable.both');
    var nameSortClass = '';
    if (sortableColumns[0].innerText == 'Name') {
        if(sortableColumns[0].classList.contains('asc')) {
            nameSortClass = 'asc';
        }
        if(sortableColumns[0].classList.contains('desc')) {
            nameSortClass = 'desc';
        }
    }

    return {'rowsPerPageDropdownIndex': rowsPerPageDropdownIndex,
            'rowsPerPageIndex': rowsPerPageIndex,
            'nameSortClass': nameSortClass
    }
}

function restoreState() {
    // making the number of rows to be same
    var dropdownElements = $('.page-list .dropdown-menu .dropdown-item');
    dropdownElements[pageState.rowsPerPageDropdownIndex].click();

    // making the same page active as was before
    var paginationElements = $('.pagination .page-item .page-link');
    paginationElements[pageState.rowsPerPageIndex].click();

    // sorting the table as it was before
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

}

function refresh() {
    if($('#search_by_worklist_name').is(":visible") == true) {
        search_term = $("#search_by_worklist_name_form input[name=search_term]").val();
        search_type = $("#search_by_worklist_name_form input[name=search_type]").val();
    } else {
        search_term = $("#search_by_username_form input[name=search_term]").val();
        search_type = $("#search_by_username_form input[name=search_type]").val();
    }

    pageState = rememberState();

    $('#worklist_table').load("/worklist-tool/update-worklist-table?search_term=" +
        encodeURIComponent(search_term) + "&search_type=" + encodeURIComponent(search_type), function(){
            $('#task_table').hide();
            setTimeout(function(){$('#worklist_table').fadeIn('slow');},0);
        }
    );
}

function worker() {
    refresh();
    setTimeout(worker, 50000);
}

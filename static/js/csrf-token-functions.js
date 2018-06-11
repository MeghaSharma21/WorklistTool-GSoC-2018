// For getting csrf token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        cookies.forEach(function (element) {
            var cookie = jQuery.trim(element);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue =
                    decodeURIComponent(cookie.substring(name.length + 1));
                return;
            }
        });
    }
    return cookieValue;
}

// To check if the method is csrf Safe
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

// Acquiring csrf token
var csrftoken = getCookie('csrftoken');

// Making sure csrf token is sent with every ajax request
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// for ajaxSetup: beforeSend
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
    
function sendTeamFund(id, fund) {    
    $.ajax({
        url: 'fund/',
        data:{
            "team_id": id,
            "fund": fund
        },
        success: function(data) {
            // console.log(data);
            location.reload();
        },
        failure: function(data) {
            console.log(data);
        }
    });
}
    
$( document ).ready(function() {    
    // setup ajax for send request to server
    $.ajaxSetup({
        type: "POST",
        
        // Setting the csrf token on the AJAX request header before being sent to other domains
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        },
        
        // prevent all future AJAX requests from being cached
        cache: false,
    });
    
    $('.btn_funding').click(function() {
        
        var id, fund;
        id = $(this).data('team-id');
        fund = $('#team_fund', $(this).closest("div.funding_panel")).val();
        sendTeamFund(id, fund);
    });
    
});
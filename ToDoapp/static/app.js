$(function () {
    $("#datetimepicker1").datetimepicker({
        format:'MM-DD-YYYY'
    });
  });

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function () {
    $("table tr td button").click(function () {
       // gets the td for which button was clicked
        var $td = $(this).closest("button"); 
        // gets the selected Attraction for that particular td
        var name_id = $td.attr("name");
        console.log(name_id);
        var csrftoken = Cookies.get('csrftoken');
        $.ajax({
            type: 'POST',
            url: 'delete/',
            headers:{
                'X-CSRFToken': csrftoken
            },
            data: {"id":name_id},
            cache: true,
            success: function(){
                $("#"+name_id).remove();
            }
        });
    });
});
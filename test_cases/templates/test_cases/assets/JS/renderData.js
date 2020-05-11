var len = $("#table").len
var i;
var data ={}
for(i=1;i<=len;i++)
{
    var temp =
    {
         kainos_id:$("#kainos_id"+i).val(),
         name:$("#name"+i).val(),
         result:$("#result"+i).val(),
         scenario:$("#scenario"+i).val()
    };
    data.append(temp);
}
alert(data);



/*$(document).ready(function(){
    $("select.result").change(function(){
        var selectedCountry = $(this).children("option:selected").val();
        var kainos_id = 'ROTP.0001'
           $.ajax(
           {
            type:"POST",
               url: "{% url 'myapp:track' %}",
               data:{
                        kainos_id: kainos_id,
                        result : selectedCountry,
                        csrfmiddlewaretoken: getCookie('csrftoken') // No traling comma

               },
               
               success: function(data) {
                 alert("Success")
              },
              error: function(data){
        alert("fail");
    }
            })
        //alert("You have selected the country - " + selectedCountry);
    });
});*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

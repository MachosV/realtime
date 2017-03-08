var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket;
$( document ).ready(function() {
    socket = new WebSocket(ws_scheme + '://' + window.location.host + "/artist_sub/");
    socket.onmessage = function(e){
        if(e.data.split(" ")[0] == "update"){
            response = e.data.slice(7)
            response = JSON.parse(response)
            obj = document.getElementById(response.name)
            delete response.name
            for (var key in response) {
                if (response.hasOwnProperty(key)) {
                    obj.children[key].innerHTML = response[key];
                }
            }
            return false;
        }
        var ul = document.getElementById("artist_list");
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(e.data));
        ul.appendChild(li);
        $(li).addClass('animated fadeInLeftBig').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',function() {
          $(this).removeClass('animated fadeInLeftBig');
        });
    }
});

$(window).on("unload", function(e) {
    socket.close();
});
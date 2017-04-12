var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket;
$( document ).ready(function() {
    socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/phones/");
    socket.onmessage = function(e){
        try{document.getElementById("no_phones").remove();}
        catch(err){}
        var ul = document.getElementById("phone_list");
        var li = document.createElement("li");
        var a = document.createElement("a");
        response = JSON.parse(e.data);
        li.id = response.imsi;
        a.href = "phone/"+response.imsi;
        a.innerText = response.imsi;
        li.appendChild(a);
        ul.appendChild(li);
        $(li).addClass('animated fadeInLeftBig').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',function() {
          $(this).removeClass('animated fadeInLeftBig');
        });
    }
});

$(window).on("unload", function(e) {
    socket.close();
});

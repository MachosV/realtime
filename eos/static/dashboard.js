var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket;

$( document ).ready(function() {
    socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/dashboard/");
    socket.onmessage = function(e){
        response = JSON.parse(e.data);
        if (response.type == 'phone'){
            handlePhone(response);
        }
        else if(response.type == 'log'){
            handleLog(response);
        }
        else{
            console.log("Unknown type")
        }
    }
});

function handlePhone(response){
    if(response.value == 'connected'){
        try{document.getElementById("no_phones").remove();}
        catch(err){}
        var ul = document.getElementById("phone_list");
        var li = document.createElement("li");
        var a = document.createElement("a");
        li.id = response.imsi;
        a.href = "phone/"+response.imsi;
        a.innerText = response.imsi;
        li.appendChild(a);
        ul.appendChild(li);
        $(li).addClass('animated fadeInLeftBig').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',function() {
          $(this).removeClass('animated fadeInLeftBig');
        });
    }
    else{
        var obj = document.getElementById(response.imsi);
        obj.parentNode.removeChild(obj);
        var ul = document.getElementById("phone_list");
        if (ul.children.length == 0){
            p = document.createElement("p");
            p.id = "no_phones";
            p.innerText = "No phones connected";
            document.getElementById("phonediv").appendChild(p);
        }
    }
}

function handleLog(response){
    var last = $('#logdiv .log-item:last-child');//last log selector, get it and remove it dramatically
    $('#logdiv').prepend("<span class='log-item'>"+response.imsi+"->"+response.field+":"+response.value+" @ "+dateFormat(new Date(response.timestamp), "mmm d, yyyy, HH:MM:ss")+"</span><br>");
    $(last).addClass('animated fadeOutDown').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',function() {
          $(this).removeClass('animated fadeOutDown');
          $(this).remove();
        });
}
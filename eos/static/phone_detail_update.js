var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket;
$( document ).ready(function() {
    socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/phone_update/"+window.location.href.split('phone/')[1]);
    socket.onmessage = function(e){
        response = JSON.parse(e.data);
        for (var key in response) {
            document.getElementById(key).innerText = response[key];
        }
    }
});

$(document).ready(sendCommand);

$(window).on("unload", function(e) {
    socket.close();
});

function sendCommand(){
    $("#commandBtn").click( function(){
        txtbox = document.getElementById("command");
        socket.send(txtbox.value);
        txtbox.value = "";
    });
}
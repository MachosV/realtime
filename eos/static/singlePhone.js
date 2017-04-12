var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var socket;
$( document ).ready(function() {
    socket = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/web/"+window.location.href.split('phone/')[1]);
    socket.onmessage = function(e){
        response = JSON.parse(e.data);
        if(response.hasOwnProperty("command")){ //check if data received is command result
            //if yes, display result, else update values
            document.getElementById("cmd-result").innerText = response.text;
        }
        else{
            for (var key in response) {
                document.getElementById(key).innerText = response[key];
            }
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
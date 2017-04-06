from websocket import create_connection
from time import sleep
imsi = "imsi1"
ws = create_connection("ws://localhost:8000/livephone/"+imsi)
tag = "RPI:"
while True:
    try:
        result =  ws.recv()
        print tag,result #works
        print tag,"Sending ok message"
        ws.send("RPI Ok, command received")
    except:
        print "Retrying connection"
        sleep(1)
ws.close()
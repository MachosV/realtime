from websocket import create_connection
from time import sleep
imsi = "test1"
ws = create_connection("ws://localhost:8000/ws/rpi/" + imsi)
while True:
    try:
        result =  ws.recv()
        print "[*]RPI received:",result
        ws.send("RPI says hello")
    except:
        print "Connection timeout"
        sleep(3)
ws.close()
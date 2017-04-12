from websocket import create_connection
from time import sleep
imsi = "test1"
try:
    ws = create_connection("ws://localhost:8001/ws/rpi/" + imsi)
except:
    ws = create_connection("ws://localhost:8000/ws/rpi/" + imsi)
while True:
    try:
        result =  ws.recv()
        print "[*]RPI received:",result
        ws.send("RPI says hello")
    except:
        sleep(1)
ws.close()
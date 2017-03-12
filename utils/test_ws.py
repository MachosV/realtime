from websocket import create_connection
imsi = "imsi1"
ws = create_connection("ws://localhost:8000/livephone/"+imsi)
while True:
    result =  ws.recv()
    print result #works
ws.close()
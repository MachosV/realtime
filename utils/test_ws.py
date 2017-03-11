from websocket import create_connection
ws = create_connection("ws://localhost:8000/test/")
ws.send("Hello, World")
while True:
    result =  ws.recv()
    print "Received '%s'" % result
ws.close()
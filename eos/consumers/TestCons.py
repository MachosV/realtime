def testOk(message):
    print message
    message.reply_channel.send({"accept": True})
    message.reply_channel.send({"text": "AT Command"})

def testDc(message):
    print "client disconnected"
from channels import Group

def phoneConnected(message):
    message.reply_channel.send({"accept": True})
    phoneId = message.content['path'].replace("/","")
    Group(phoneId).add(message.reply_channel)

def phoneDisconnected(message):
    phoneId = message.content['path'].replace("/", "")
    Group(phoneId).discard(message.reply_channel)
    #inform UI that phone disconnected

def sendCommand(message):
    phoneId = message.content['path'].replace("/", "").replace("phone_update","livephone")
    Group(phoneId).send({
        "text": message.content['text']
    })
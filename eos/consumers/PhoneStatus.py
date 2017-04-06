from channels import Group
import json

def phoneConnected(message):
    message.reply_channel.send({"accept": True})
    phoneId = message.content['path'].replace("/","")
    Group(phoneId).add(message.reply_channel)

def phoneDisconnected(message):
    phoneId = message.content['path'].replace("/", "")
    Group(phoneId).discard(message.reply_channel)
    #inform UI that phone disconnected

def sendCommandToRPI(message):
    phoneId = message.content['path'].replace("/", "").replace("phone_update", "livephone")
    Group(phoneId).send({
        "text": message.content['text']
    })

def sendCommandToWeb(message):
    data = {}
    data['command'] = True
    data['text'] = message.content['text']
    id = message.content['path'].split("/")[2]
    data = json.dumps(data)
    Group(id).send({
        "text": data
    })
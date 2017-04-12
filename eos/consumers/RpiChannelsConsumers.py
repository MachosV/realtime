from channels import Group
import json

def rpiConnected(message):
    message.reply_channel.send({"accept": True})
    rpi = message.content['path'].replace("/","")
    print "[*]Connected to:",rpi
    Group(rpi).add(message.reply_channel)

def rpiDisconnected(message):
    rpi = message.content['path'].replace("/","")
    print "[*]Disconnected from:", rpi
    Group(rpi).discard(message.reply_channel)

def rpi2web(message):
    data = {}
    data['command'] = True
    data['text'] = message.content['text']
    data = json.dumps(data)
    web = message.content['path'].replace("rpi","web").replace("/","")
    Group(web).send({
        "text": data
    })


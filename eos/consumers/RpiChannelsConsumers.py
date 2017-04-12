from channels import Group
import json
from utils.PhoneConnected import phoneConnected,phoneDisconnected

def rpiConnected(message):
    message.reply_channel.send({"accept": True})
    rpi = message.content['path'].replace("/","")
    Group(rpi).add(message.reply_channel)
    phoneConnected(message)

def rpiDisconnected(message):
    rpi = message.content['path'].replace("/","")
    Group(rpi).discard(message.reply_channel)
    phoneDisconnected(message)

def rpi2web(message):
    data = {}
    data['command'] = True
    data['text'] = message.content['text']
    data = json.dumps(data)
    web = message.content['path'].replace("rpi","web").replace("/","")
    Group(web).send({
        "text": data
    })


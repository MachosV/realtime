from channels import Group
import json

def subscribeWebChannel(message):
    message.reply_channel.send({"accept": True})
    web_channel = message.content['path'].replace("/","")
    Group(web_channel).add(message.reply_channel)

def unsubscribeWebChannel(message):
    Group(message.content['path'].replace("/","")).discard(message.reply_channel)

def updatePhone(newData):
    web_channel = "wsweb"+newData['imsi']
    try:
        Group(web_channel).send({
            "text":json.dumps(newData)
        })
    except:
        print "sumfink gouent ronk"

def web2rpi(message):
    rpi_channel = message.content['path'].replace("/","").replace("web","rpi")
    Group(rpi_channel).send({
        "text": message.content['text']
    })

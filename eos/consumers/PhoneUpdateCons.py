from channels import Group
import json

def subscribeSinglePhone(message):
    message.reply_channel.send({"accept": True})
    imsi = message.content['path'].split("phone_update/")[1][:-1]
    Group(imsi).add(message.reply_channel)

def unsubscribeSinglePhone(message):
    Group(message.content['path'].split("phone_update/")[1][:-1]).discard(message.reply_channel)

def updatePhone(newData):
    try:
        print newData['imsi'] #updating to group with name imsi
        Group(newData['imsi']).send({
            "text":json.dumps(newData)
        })
    except:
        print "sumfink gouent ronk"
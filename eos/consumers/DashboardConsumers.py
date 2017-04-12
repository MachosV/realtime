from channels import Group
import json

def subscribeDashboard(message):
    message.reply_channel.send({"accept": True})
    Group("Dashboard").add(message.reply_channel)

def unsubscribeDashboard(message):
    Group("Dashboard").discard(message.reply_channel)

def notifyDashboard(data):
    Group("Dashboard").send({
        "text": data
    })
from channels import Group

def subscribePhones(message):
    print "subscribed on phones"
    Group("phones").add(message.reply_channel)
    message.reply_channel.send({
        "accept": True, #needed for successful handshake
    })

def unsubscribePhones(message):
    Group("phones").discard(message.reply_channel)

def updatePhone(newData):
    Group("phones").send({
        "text":"update"+" "+newData
    })

def notifyNewPhone(newPhone):
    Group("phones").send({
        "text":newPhone.get_self()
    })
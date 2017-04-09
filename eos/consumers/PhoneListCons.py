from channels import Group

def subscribePhones(message):
    print "CONSUMER: Web connection OK!"
    Group("phones").add(message.reply_channel)
    message.reply_channel.send({
        "accept": True, #needed for successful handshake
    })

def unsubscribePhones(message):
    Group("phones").discard(message.reply_channel)

def notifyNewPhone(newPhone): #deployment comment, consumer receives message
    Group("phones").send({
        "text":newPhone.get_self()
    })

from channels import Group

def subscribePhoneList(message):
    Group("phones").add(message.reply_channel)
    message.reply_channel.send({
        "accept": True, #needed for successful handshake
    })

def unsubscribePhoneList(message):
    Group("phones").discard(message.reply_channel)

def notifyNewPhone(newPhone):
    Group("phones").send({
        "text":newPhone.get_self()
    })

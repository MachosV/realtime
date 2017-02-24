from channels import Group

def subscribeArtists(message):
    Group("artists").add(message.reply_channel)
    message.reply_channel.send({
        "accept": True,
    })

def unsubscribeArtists(message):
    Group("artists").discard(message.reply_channel)

def notifyNewArtist(newArtist):
    print newArtist
    Group("artists").send({
        "text":newArtist.name
    })
from channels.routing import route,include
from eos.consumers import subscribePhones,unsubscribePhones

part_routing = [
    route("websocket.connect", subscribePhones),
    route("websocket.disconnect", unsubscribePhones),
]

channel_routing = [
    include(part_routing, path =r"^/phone_sub/")
]
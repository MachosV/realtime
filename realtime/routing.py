from channels.routing import route,include
from eos.consumers import *

phone_list_routing = [
    route("websocket.connect", subscribePhones),
    route("websocket.disconnect", unsubscribePhones),
]

phone_update_routing = [
    route("websocket.connect", subscribeSinglePhone),
    route("websocket.disconnect", unsubscribePhones),
]

channel_routing = [
    include(phone_list_routing, path = r"^/phone_sub/"),
    include(phone_update_routing, path =r'^/phone_update/' )
]
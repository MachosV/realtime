from channels.routing import route,include
from eos.consumers import *

phone_list_routing = [
    route("websocket.connect", subscribePhones),
    route("websocket.disconnect", unsubscribePhones),
]

phone_update_routing = [
    route("websocket.connect", subscribeSinglePhone),
    route("websocket.disconnect", unsubscribePhones),
    route("websocket.receive",sendCommandToRPI),
]

phone_status_routing = [
    route("websocket.connect",phoneConnected),
    route("websocket.disconnect",phoneDisconnected),
    route("websocket.receive",sendCommandToWeb)
]

channel_routing = [
    include(phone_list_routing, path = r"^/phone_sub/"),
    include(phone_update_routing, path = r'^/phone_update/' ),
    include(phone_status_routing, path = r'^/livephone/'),
]
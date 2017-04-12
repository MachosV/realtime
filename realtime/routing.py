from channels.routing import route,include
from eos.consumers import *

#routing for phonelist
phone_list = [
    route("websocket.connect", subscribePhoneList),
    route("websocket.disconnect", unsubscribePhoneList),
]

#routing web interface 2 rpi
web_channels = [
    route("websocket.connect", subscribeWebChannel),
    route("websocket.disconnect", unsubscribeWebChannel),
    route("websocket.receive",web2rpi),
]

#routing rpi to web interface
rpi_channels = [
    route("websocket.connect",rpiConnected),
    route("websocket.disconnect",rpiDisconnected),
    route("websocket.receive",rpi2web)
]

dashboard_channel = [
    route("websocket.connect",subscribeDashboard),
    route("websocket.disconnect",unsubscribeDashboard),
]

channel_routing = [
    include(phone_list, path = r"^/ws/phones/"),
    include(web_channels, path = r'^/ws/web/' ),
    include(rpi_channels, path = r'^/ws/rpi/'),
    include(dashboard_channel,path = r'^/ws/dashboard'),
]
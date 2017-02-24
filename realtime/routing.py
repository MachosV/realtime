from channels.routing import route,include
from eos.consumers import subscribeArtists,unsubscribeArtists


part_routing = [
    route("websocket.connect", subscribeArtists),
    route("websocket.disconnect", unsubscribeArtists),
]

channel_routing = [
    include(part_routing, path =r"^/artist_sub/")
]
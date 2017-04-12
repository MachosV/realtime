from eos.models import LivePhone,Phone
from eos.consumers.DashboardConsumers import notifyDashboard
import json
#connected to websocket, create live phone object and notify UI
def phoneConnected(data):
    imsi = data.content['path'].split("/")[3]
    phone = Phone.objects.get(imsi = imsi)
    live_phone = LivePhone(phone = phone)
    live_phone.save()
    data = {}
    data['imsi'] = imsi
    data['type'] = "phone"
    data['value'] = "connected"
    data = json.dumps(data)
    notifyDashboard(data)

#connected to websocket, delete live phone and notify UI
def phoneDisconnected(data):
    imsi = data.content['path'].split("/")[3]
    LivePhone.objects.get(phone=Phone.objects.get(imsi=imsi)).delete()
    data = {}
    data['imsi'] = imsi
    data['type'] = "phone"
    data['value'] = 'disconnected'
    data = json.dumps(data)
    notifyDashboard(data)

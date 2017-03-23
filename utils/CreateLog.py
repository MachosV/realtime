from eos.models import Log
import datetime

def createLog(data):
    imsi = data['imsi']
    timestamp = data.get('timestamp',datetime.datetime.now())
    data.pop('imsi', None)
    data.pop('timestamp', None)
    for key,value in data.iteritems():
        log = Log()
        log.imsi = imsi
        log.timestamp = timestamp
        log.field = key
        log.value = value
        log.save()
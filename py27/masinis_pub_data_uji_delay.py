import paho.mqtt.client as mqtt
import json
import time
import datetime

mqttc = mqtt.Client("publisher_uji", clean_session=False)
ip_broker = "127.0.0.1"
port = 1883
mqttc.connect(ip_broker, port)
i = 1
while (i == 1):
    id_rfid = str(raw_input("Masukkan ID tag : "))
    # Uji waktu pake ctime
    waktu_ctime = str(time.ctime())
    # Uji waktu pake datetime
    x = datetime.datetime.now()
    pub_detik = x.second
    pub_microsecond = x.microsecond
    waktu_datetime = str(str(pub_detik)+" : "+str(pub_microsecond))

    dictionary_pengujian = {
        "id_rfid": id_rfid,
        "waktu_ctime":waktu_ctime,
        "waktu_datetime": waktu_datetime
    }
    # MEMBUNGKUS JADI JSON
    json_pengujian = json.dumps(dictionary_pengujian)
    # MELAKUKAN PUBLISHING
    topik = "rfid/readrfid/position/pengujian"
    qos = 1
    mqttc.publish(topic=topik, payload=json_pengujian, qos=qos, retain=False)
    print json_pengujian
    i = 1

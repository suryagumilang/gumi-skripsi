import paho.mqtt.client as mqtt
import json

mqttc = mqtt.Client("masinis_ujiketelitian", clean_session=False)
ip_broker = "127.0.0.1"
port = 1883
mqttc.connect(ip_broker, port)
i = 1
while (i == 1):
    id_rfid = str(raw_input("Masukkan ID tag : "))

    dictionary_pemantauan = {
        "id_rfid": id_rfid,
    }
    # MEMBUNGKUS JADI JSON
    json_pemantauan = json.dumps(dictionary_pemantauan)
    # MELAKUKAN PUBLISHING
    topik = "rfid/readrfid/position/ujiketelitian"
    qos = 1
    mqttc.publish(topic=topik, payload=json_pemantauan, qos=qos, retain=False)
    print json_pemantauan
    i = 1
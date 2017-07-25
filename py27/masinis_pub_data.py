# KODE PROGRAM MENGGUNAKAN PYTHON 2.7x

# IMPORT LIBRARY
# -PAHO.MQTT
# -JSON
# -TIME
import paho.mqtt.client as mqtt
import json
import time

# INISIALISASI CLIENT MQTT
mqttc = mqtt.Client("masinis_pub1", clean_session=False)
# MEMBUAT KONEKSI KE BROKER
ip_broker = "127.0.0.1"
port = 1883
mqttc.connect(ip_broker, port)
# mqttc.connect("127.0.0.1", 1883)

i = 1
while (i == 1):
    id_rfid = str(raw_input("Masukkan ID tag : "))
    no_ka = "101"
    nama_ka = "Malioboro Ekspress"
    waktu = str(time.ctime())

    # DATA DIATAS DIJADIKAN DICTIONARY
    dictionary_pemantauan = {
        "id_rfid": id_rfid,
        "no_ka": no_ka,
        "nama_ka": nama_ka,
        "waktu": waktu
    }
    # MEMBUNGKUS JADI JSON
    json_pemantauan = json.dumps(dictionary_pemantauan)

    # MELAKUKAN PUBLISHING
    topik = "rfid/readrfid/position/" + no_ka
    qos = 1
    mqttc.publish(topic=topik, payload=json_pemantauan, qos=qos, retain=False)
    print json_pemantauan

    i = 1

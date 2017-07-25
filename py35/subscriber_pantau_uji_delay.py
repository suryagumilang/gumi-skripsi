import paho.mqtt.client as mqtt
import pymysql
import json
import threading
import time
import datetime

mqttc = mqtt.Client("subscriber_uji", clean_session=False)

class connectDB:
    def __init__(self, id_rfid, pub_waktu_ctime, pub_waktu_datetime, sub_waktu_ctime, sub_waktu_datetime):
        self.id_rfid = id_rfid
        self.pub_waktu_ctime = pub_waktu_ctime
        self.pub_waktu_datetime = pub_waktu_datetime
        self.sub_waktu_ctime = sub_waktu_ctime
        self.sub_waktu_datetime = sub_waktu_datetime

    def getData(self):
        id_rfid = self.id_rfid
        pub_waktu_ctime = self.pub_waktu_ctime
        pub_waktu_datetime = self.pub_waktu_datetime
        sub_waktu_ctime = self.sub_waktu_ctime
        sub_waktu_datetime = self.sub_waktu_datetime

        print("ID RFID : "+id_rfid)
        print("Waktu menggunakan ctime")
        print("Waktu di publisher   : "+pub_waktu_ctime)
        print("Waktu di subscriber  : "+sub_waktu_ctime)
        print("Waktu menggunakan datetime")
        print("Waktu di publisher   : "+pub_waktu_datetime)
        print("Waktu di subscriber  : "+sub_waktu_datetime)
        print("--------------------------------------------")

def pesan_masuk(mqttc, obj, msg):
    dictionary_pengujian = json.loads(msg.payload.decode('utf-8'))  # Untuk json load pada Python 3
    id_rfid = dictionary_pengujian["id_rfid"]
    pub_waktu_ctime = dictionary_pengujian["waktu_ctime"]
    pub_waktu_datetime = dictionary_pengujian["waktu_datetime"]
    # Membuat waktu subscriber
    sub_waktu_ctime = str(time.ctime())
    x = datetime.datetime.now()
    sub_detik = x.second
    sub_microsecond = x.microsecond
    sub_waktu_datetime = str(sub_detik)+" : "+str(sub_microsecond)
    connect = connectDB(str(id_rfid), pub_waktu_ctime, pub_waktu_datetime, sub_waktu_ctime, sub_waktu_datetime)
    connect.getData()

mqttc.on_message = pesan_masuk
# MEMBUAT KONEKSI KE BROKER MQTT
ip_broker = "127.0.0.1" #IP broker
port = 1883
mqttc.connect(ip_broker, port)

def subscribing(topic, qos):
    topic = topic
    qos = qos
    mqttc.subscribe(topic, qos=qos)
    print("Subscriber ready")
    print("=======================================")

try:
    topic = "rfid/readrfid/position/pengujian"
    qos = 1
    t = threading.Thread(target=subscribing(topic, qos))
except:
    print("Error thread")

mqttc.loop_forever()

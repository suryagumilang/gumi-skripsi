import paho.mqtt.client as mqtt
import pymysql
import json
import threading

mqttc = mqtt.Client("sub_ujiketelitian", clean_session=False)

class connectDB:
    def __init__(self, id_rfid):
        self.id_rfid = id_rfid

    def getData(self):
        id_rfid = self.id_rfid

        # MEMBUAT KONEKSI KE DB
        con = pymysql.connect(
            db="db_sistempemantauanv4x",  # nama database
            user="root",
            passwd="",
            host="localhost",  # IP dari db server
            port=3306,
            autocommit=True
        )
        cur = con.cursor()
        # SQL UNTUK MENGAMBIL DATA DARI DATABASE
        sql_get = "SELECT * from `pengujian` WHERE `id_rfid` = '%s'" % id_rfid
        try:
            cur.execute(sql_get)
            data = cur.fetchone()
            id_rfid = data[0]
            posisi = data[1]
            print("ID RFID  : " + id_rfid+" || Posisi   : "+posisi)
            print("---------------------------")
            con.commit()

        except:  # JIKA EKESEKUSI SQL GAGAL
            print("---------------------")
            print("     Not valid !!")
            print("---------------------")

def pesan_masuk(mqttc, obj, msg):
    dictionary_pemantauan = json.loads(msg.payload.decode('utf-8'))
    id_rfid = dictionary_pemantauan["id_rfid"]
    connect = connectDB(str(id_rfid))
    connect.getData()

mqttc.on_message = pesan_masuk

# MEMBUAT KONEKSI KE BROKER MQTT
ip_broker = "127.0.0.1" #IP broker
port = 1883
mqttc.connect(ip_broker, port)

# MELAKUKAN SUBSCRIBING DENGAN TOPIK TERTENTU
def subscribing(topic, qos):
    topic = topic
    qos = qos
    # mqttc.subscribe("rfid/readrfid/position/#", qos=1)
    mqttc.subscribe(topic, qos=qos)
    print("Pengujian ketelitian siap !")
    print("=======================================")

# MEMBUAT THREAD
try:
    topic = "rfid/readrfid/position/ujiketelitian"
    qos = 1
    t = threading.Thread(target=subscribing(topic, qos))
except:
    print("Error thread")

mqttc.loop_forever()
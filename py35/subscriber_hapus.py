# BARIS KODE MENGGUNAKAN PYTHON 3.5x

# IMPORT LIBRARY:
# - PAHO.MQTT
# - PYMYSQL
# - JSON
import paho.mqtt.client as mqtt
import pymysql
import json

# INISIALISASI MQTT CLIENT
mqttc = mqtt.Client("sub_hapus", clean_session=False)


# CLASS UNTUK BERHUBUNGAN DENGAN DB
class connectDB:
    def __init__(self, no_ka, nama_ka):
        self.no_ka = no_ka
        self.nama_ka = nama_ka

    # FUNGSI UNTUK MENGHAPUS
    def delData(self):
        no_ka = self.no_ka
        nama_ka = self.nama_ka

        # MEMBUAT KONEKSI KE DB
        con = pymysql.connect(
            db="db_sistempemantauanv4",  # nama database
            user="root",
            passwd="",
            host="localhost",  # IP dari db server
            port=3306,
            autocommit=True
        )
        cur = con.cursor()

        # SQL UNTUK MENGHAPUS KE DB
        sql_hapus = "DELETE FROM `history` WHERE `no_ka` = '%s'" % no_ka
        try:
            cur.execute(sql_hapus)  # MENJALANKAN SQL-NYA
            con.commit()
            print("Hapus data perjalanan untuk KA " + no_ka + " " + nama_ka + " berhasil")
            print(cur._last_executed)
        except:
            con.rollback()
            print("Hapus data perjalanan untuk KA " + no_ka + " " + nama_ka + " gagal")
            print(cur._last_executed)


# MENGINISIASI FUNGSI CALLBACK
def pesan_hapus(mqttc, obj, msg):
    dictionary_hapus = json.loads(msg.payload.decode('utf-8'))
    no_ka = dictionary_hapus["no_ka"]
    nama_ka = dictionary_hapus["nama_ka"]
    connect = connectDB(no_ka, nama_ka)
    connect.delData()


# MENDAFTARKAN FUNGSI CALLBACK
mqttc.on_message = pesan_hapus

# MEMBUAT KONEKSI KE BROKER
ip_broker = "127.0.0.1"  # IP broker
port = 1883
mqttc.connect(ip_broker, port)

# MELAKUKAN SUBSCRIBING DENGAN TOPIK TERTENTU
mqttc.subscribe("rfid/hapus/#", qos=1)
print("Siap menghapus")
print("=======================================")

# Looping subscriber
mqttc.loop_forever()

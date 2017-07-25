# BARIS KODE MENGGUNAKAN PYTHON 3.5x

# IMPORT LIBRARY:
# - PAHO.MQTT
# - PYMYSQL
# - JSON
# - THREAD / THREADING
import paho.mqtt.client as mqtt
import pymysql
import json
import threading

# INISIALISASI CLIENT MQTT
mqttc = mqtt.Client("sub_pantau", clean_session=False)


# CLASS UNTUK BERHUBUNGAN DENGAN DATABASE
class connectDB:
    def __init__(self, id_rfid, no_ka, nama_ka, waktu):
        self.id_rfid = id_rfid
        self.no_ka = no_ka
        self.nama_ka = nama_ka
        self.waktu = waktu

    def getData(self):
        id_rfid = self.id_rfid
        no_ka = self.no_ka
        nama_ka = self.nama_ka
        waktu = self.waktu

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
        # SQL UNTUK MENGAMBIL DATA DARI DATABASE
        sql_get = "SELECT * from `pantau` WHERE `id_rfid` = '%s'" % id_rfid
        try:
            cur.execute(sql_get)
            data = cur.fetchone()

            id_rfid = data[0]
            is_stasiun = data[1]
            nama_lokasi = data[2]
            gmaps_ls = data[3]
            gmaps_bt = data[4]
            real_ls = data[5]
            real_bt = data[6]
            kota_kab = data[7]
            provinsi = data[8]
            jalur = data[9]
            no_ka = no_ka
            nama_ka = nama_ka
            waktu = waktu

            #  PRINT DATA
            print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            print('Nomor KA     : ' + no_ka)
            print('Nama KA      : ' + nama_ka)
            if is_stasiun == "YA":
                print('Kereta api sedang berada pada stasiun')
                print(nama_lokasi)
                print('Jalur    : ' + jalur)
            else:
                print('Kereta api sedang tidak pada stasiun')
                print('Posisi kereta api ' + nama_lokasi)
            print('     Koordinat Kereta Api   ')
            print('Google Maps       : ' + gmaps_ls + ' Lintang Selatan dan ' + gmaps_bt + ' Bujur Timur')
            print('Peta Konvensional : ' + real_ls + ' Lintang Selatan dan ' + real_bt + ' Bujur Timur')
            print('Kota / Kabupaten  : ' + kota_kab)
            print('Provinsi          : ' + provinsi)
            if jalur == "In Out":
                print('     PERHATIAN !!!')
                print('Kereta pada posisi In / Out stasiun')
            else:
                print('Jalur In / Out stasiun aman')
            print('Waktu Terakhir    : ' + waktu)
            print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

            # SETELAH GET DATA, DATA AKAN DISIMPANG KE TABLE HISTORY
            cur.execute("""
    INSERT INTO history (id_rfid, nama_ka, no_ka, is_stasiun, nama_lokasi, gmaps_ls, gmaps_bt, real_ls, real_bt, kota_kab, provinsi, jalur, waktu)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", (id_rfid, nama_ka, no_ka, is_stasiun, nama_lokasi, gmaps_ls, gmaps_bt, real_ls, real_bt, kota_kab, provinsi, jalur,
      waktu))
            con.commit()

        except:  # JIKA EKESEKUSI SQL GAGAL
            print("---------------------")
            print("     Not valid !!")
            print("---------------------")


# FUNGSI UNTUK MENANGANI PESAN MASUK
def pesan_masuk(mqttc, obj, msg):
    dictionary_pemantauan = json.loads(msg.payload.decode('utf-8'))  # Untuk json load pada Python 3
    id_rfid = dictionary_pemantauan["id_rfid"]
    no_ka = dictionary_pemantauan["no_ka"]
    nama_ka = dictionary_pemantauan["nama_ka"]
    waktu = dictionary_pemantauan["waktu"]
    connect = connectDB(str(id_rfid), no_ka, nama_ka, waktu)
    connect.getData()


# MENDAFTARKAN FUNGSI CALLBACK
mqttc.on_message = pesan_masuk

# MEMBUAT KONEKSI KE BROKER MQTT
ip_broker = "127.0.0.1" #IP broker
port = 1883
mqttc.connect(ip_broker, port)


# mqttc.connect("iot.eclipse.org", 1883)

# MELAKUKAN SUBSCRIBING DENGAN TOPIK TERTENTU
def subscribing(topic, qos):
    topic = topic
    qos = qos
    # mqttc.subscribe("rfid/readrfid/position/#", qos=1)
    mqttc.subscribe(topic, qos=qos)
    print("Subscriber ready")
    print("=======================================")


# MEMBUAT THREAD
try:
    topic = "rfid/readrfid/position/#"
    qos = 1
    t = threading.Thread(target=subscribing(topic, qos))
except:
    print("Error thread")

# Looping subscriber
mqttc.loop_forever()

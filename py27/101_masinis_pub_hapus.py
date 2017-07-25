# KODE PROGRAM MENGGUNAKAN PYTHON 2.7x
# IMPORT LIBRARY YANG DIGUNAKAN
# -TKINTER
# -JSON
# -PAHO.MQTT
from Tkinter import *
import tkMessageBox
import json
import paho.mqtt.client as mqtt
import time

# UNTUK KERETA 101 - MALIOBORO EKSPRESS

# INISIALISASI CLIENT MQTT
mqttc = mqtt.Client("masinis_pub_hapus1", clean_session=False)
# MEMBUAT KONEKSI KE BROKER
ip_broker = "127.0.0.1"
port = 1883
mqttc.connect(ip_broker, port)

# MEMBANGKITKAN GUI-NYA
gui = Tk()
gui.geometry("300x350")

label = Label(gui, text="KA 101 - Malioboro Ekspress", relief=RAISED)
label.pack(side=TOP, pady=10)

# Method untuk mengerjakan delete data
def berhenti():
    no_ka = "101"
    nama_ka = "Malioboro Ekspress"
    # Data dijadikan dictionary
    dictionary_hapus = {
        "no_ka":no_ka,
        "nama_ka":nama_ka
    }
    json_hapus = json.dumps(dictionary_hapus)

    topik = "rfid/hapus/"+no_ka
    qos = 1
    mqttc.publish(topic=topik, payload = json_hapus, qos = qos, retain=False)#topik untuk menghapus

    tkMessageBox.showinfo("Berhenti", "Anda telah menekan tombol Berhenti !")

text = "Tombol ini hanya digunakan saat perjalanan sudah selesai"
msg = Message(gui, text = text)
msg.config(font=('times', 22, 'bold'), justify=CENTER)
msg.pack()

# Menghandle tombol
btn = Button(gui, text = "Berhenti", command=berhenti)
btn.place(x=50,y=50)
btn.pack(side=BOTTOM, pady=10)

gui.mainloop()
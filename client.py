import pyaudio as pa
import socket as sck
import time
from pvt_conf.py import *

def callback(in_data, frame_count, time_info, status):
    data=client.recv(CHUNK)
    return (data,pa.paContinue)

def _list_device():
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)["name"])

def main():
    c=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    c.bind((server_ip,5050))
    while (1):
        try:
            c.connect((bt_mac, 4))

            p = pa.PyAudio()
            stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        stream_callback=callback)

            while stream.is_active():
                time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            stream.close()
            p.terminate()

    c.close()

main()

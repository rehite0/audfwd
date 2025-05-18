import pyaudio as pa
import socket as sck
import time
from pvt_conf.py import *

def callback(in_data, frame_count, time_info, status):
    client.send(in_data)
    return (None,pa.paContinue)

def _list_device():
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)["name"])

def main():
    s=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind((sck.gethostbyname(sck.gethostname()),5050))
    s.listen(1)

    
    while (1):
        client, addr =s.accept()
        try:
            p = pa.PyAudio()
            stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        input_device_index=devno,
                        stream_callback=callback)

            while stream.is_active():
                time.sleep(1) 
        except Exception as e:
            print(e)
        finally:
            stream.close()
            p.terminate()
            client.close()
    s.close()

main()

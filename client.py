import pyaudio as pa
import socket as sck
import time
from pvt_conf import *

buff=b''
c=None
def callback(in_data, frame_count, time_info, status):
    global buff
    data=buff[:frame_count*CHANNELS*2]
    buff=buff[frame_count*CHANNELS*2:]
    #print(data,'\n\n')
    #time.sleep(2)
    #buff=buff[frame_count*CHANNELS*2:]
    return (data,pa.paContinue)

def _list_device():
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)["name"])

def main():
    global c,buff
    c=sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    while (1):
        try:
            c.connect((server_ip,5050))

            p = pa.PyAudio()
            stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        stream_callback=callback)
            while stream.is_active():
                buff+=c.recv(100)
        except Exception as e:
            print(e)
            raise e
        finally:
            stream.close()
            p.terminate()

    c.close()

main()

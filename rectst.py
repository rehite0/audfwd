import pyaudio as pa
import wave as wav
import time

p = pa.PyAudio()

for i in range(p.get_device_count()):
    print(i, p.get_device_info_by_index(i)["name"])

FORMAT = pa.paInt16
CHANNELS = 2
RATE = 48000
CHUNK = 512
RECORD_SECONDS = 5
PATH = "tmp.wav"

frames = []
def callback(in_data, frame_count, time_info, status):
        frames.append(in_data) 
        # If len(data) is less than requested frame_count, PyAudio automatically
        # assumes the stream is finished, and the stream stops.
        return (None,pa.paContinue)
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=6,
                stream_callback=callback)
'''
for _ in range(int((RATE / CHUNK) * RECORD_SECONDS)):
    print('hi')
    data = stream.read(CHUNK)
    frames.append(data)
'''
#while stream.is_active():
time.sleep(RECORD_SECONDS)
stream.close()
p.terminate()

wf = wav.open(PATH, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b"".join(frames))
wf.close()

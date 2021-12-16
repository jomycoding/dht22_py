from dht import DHT22
from machine import Pin
from time import sleep


dht = DHT22(Pin(16))

 
def loop():
  while(1):
    try:
      dht.measure()
      t = dht.temperature()
      h = dht.humidity()
      print('온도: %.1f℃  습도: %.1f%%' % (t, h))
    except:
      pass

    sleep(2)

loop()

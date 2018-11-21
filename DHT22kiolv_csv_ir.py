#!/usr/bin/env python3
print("hőmérséklet kiolvasás")

import Adafruit_DHT
import sys
import csv
import datetime
from gpiozero import LED
import time

lampa = LED(17)
sensor = Adafruit_DHT.DHT22
pin = 4

homerseklet, paratartalom = Adafruit_DHT.read_retry(sensor, pin)

# homerseklet = ("{0:0.1f}".format(homerseklet))

if homerseklet is None:
	for i in range(10):
		lampa.on()
		time.sleep(1)
		lampa.off()
		time.sleep(1)

ido = str(datetime.datetime.now())
ido = ido[:-7]
#print (ido)

dir = "/home/pi/teszt/"
f = open(dir+"database.csv" , 'at')
try:
	w = csv.writer(f, delimiter=';')
	w.writerow(("RP03_01", ido, "{0:0.1f}".format(homerseklet) , "{0:0.1f}".format( paratartalom)))
	lampa.on()
	time.sleep(2)
	lampa.off()

except:
	for i in range(3):
		led.on()
		time.sleep(1)
		led.off()
		time.sleep(1)

finally:
	f.close()
 
#print ("RP03_01", ido, "{0:0.1f}".format(homerseklet) , "{0:0.1f}".format(paratartalom))

#!/usr/bin/env python3

import Adafruit_DHT
import sys
import csv
import datetime
from gpiozero import LED
import time

#LED GPIO összerendelés
lampa = LED(17)

#szenzor
sensor = Adafruit_DHT.DHT22
pin = 4

#hőmérséklet, páratartalom beolvasás
homerseklet, paratartalom = Adafruit_DHT.read_retry(sensor, pin)

#hibakezelés nincs jel szenzorról - LED 10x felvillan
if homerseklet is None:
	for i in range(10):
		lampa.on()
		time.sleep(1)
		lampa.off()
		time.sleep(1)

#szenzor kiolvasás dátuma és ideje
ido = str(datetime.datetime.now())
ido = ido[:-7]

#a fájl ill. csv fájl elérési útvonala
dir = "/home/pi/teszt/"
f = open(dir+"database.csv" , 'at')

#fájlírás hibakezeléssel - LED 3x felvillan - sikeres írás esetén 1x2 sec-ot világít
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

#szükség esetén a fájlírás adatainak kiíratása:
#print ("RP03_01", ido, "{0:0.1f}".format(homerseklet) , "{0:0.1f}".format(paratartalom))

import RPi.GPIO as GPIO
import time

def reading(sensor, TRIG, ECHO):
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)

    if sensor == 0:
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
          signaloff = time.time()

        while GPIO.input(ECHO) == 1:
          signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
        GPIO.cleanup()

import datetime

trig = []
echo = []

trig.append(38) #migisita
echo.append(40)

trig.append(33) #migiue
echo.append(35)

trig.append(29) #hidarisita
echo.append(31)

trig.append(11)  #hidariue
echo.append(13)

import sqlite3
con = sqlite3.connect('/home/romasw/Akiwa-girl/akiwagirl/db.sqlite3')
cur = con.cursor()
occupancies = [0 for _ in range(18)]
for i in range(4):
  if reading(0, trig[i], echo[i]) <= 10:
    occupancies[i] = 1
for i, occupancy in enumerate(occupancies):
  cur.execute("UPDATE seat_occupancy set occupancy={} where id={};".format(occupancy,i+1))

con.commit()
con.close()

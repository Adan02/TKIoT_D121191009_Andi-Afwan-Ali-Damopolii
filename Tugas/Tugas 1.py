from machine import Pin
import time

PIRIn= Pin(5,Pin.IN)
Buzzer = Pin(13,Pin.OUT)

while True:
    print(p.value())
    if p.value()==1:
        o.on()
    if p.value()==0:
        o.off()
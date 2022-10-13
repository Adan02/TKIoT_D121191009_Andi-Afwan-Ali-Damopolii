from machine import Pin
import time

PIRIn= Pin(5,Pin.IN)
Buzzer = Pin(13,Pin.OUT)

while True:
    if PIRIn.value()==1:
        Buzzer.on()
    if PIRIn.value()==0:
        Buzzer.off()
    print(p.value())
    time.sleep(1)

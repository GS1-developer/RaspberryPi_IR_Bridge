
from gpiozero import LED
from time import sleep

led = LED(14)

while True:
    print("On")
    led.on()
    sleep(1)
    print("Off")
    led.off()
    sleep(1)

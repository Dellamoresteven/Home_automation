
from gpiozero import LED
from time import sleep

blue = LED(26)
red   = LED(19)
green  = LED(13)

green.off()
red.off()
blue.off()
sleep(1)

def turnOn():
    green.on()

def turnOff():
    green.off()
    red.off()
    blue.off()

print("On")
green.on()
blue.on()
red.on()
sleep(5)

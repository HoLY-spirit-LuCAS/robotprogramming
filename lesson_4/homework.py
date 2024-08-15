from neopixel import NeoPixel
from microbit import pin0
from microbit import sleep

def zapni(cislo_led):
    zmen_barvu(cislo_led , (255, 255, 255))
def vypni(poradi_led):
    zmen_barvu(cislo_led , (0, 0, 0))

def nastav_barvu(cislo_led, barva):
    np[cislo_led]=(barva)
    np.write()

np = NeoPixel(pin0,8)
#TODO: predelejte smycku tak, aby volala vyse definovane funkce
while True:
    zapni(0)
    sleep(1000)
    vypni(0)
    sleep(1000)


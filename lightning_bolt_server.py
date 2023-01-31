import time
from ledStrip import *
from config import *
from flask import Flask

def turn_on_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, GREEN)
    strip.stripShow()

def turn_off_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, [0,0,0])
    strip.stripShow()

def blink(strip):
    turn_on_leds(strip)
    time.sleep(0.5)
    turn_off_leds(strip)
    time.sleep(2)

def animate_leds():
    lstrip = LedStrip(LED_COUNT, GPIO_PIN)

    blink(lstrip)
    blink(lstrip)

    turn_on_leds(lstrip)
    time.sleep(120)
    turn_off_leds(lstrip)


app = Flask(__name__)

@app.route("/")
def start_leds():
    animate_leds()
    return "turned on leds"

import time
from ledStrip import *
from config import *
sys.path.append(os.getcwd() + "/../audio-fingerprint-identifying-python/")
from recognizer import *

def turn_on_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, GREEN)
    strip.stripShow()

def turn_off_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, GREEN)
    strip.stripShow()

def blink(strip):
    turn_on_leds(strip)
    time.sleep(0.5)
    turn_off_leds(strip)
    time.sleep(2)

def animate_leds():
    lStrip = LedStrip(LED_COUNT)

    blink(lStrip)
    blink(lStrip)

    turn_on_leds(lStrip)
    time.sleep(120)
    turn_off_leds(lStrip)


def run_audio_recognition():
    listen_length = 5
    recognition_result = recognize(listen_length)

    if recognition_result["match_found"] == True and recognition_result["accuracy"] > 40:
        return True

def acdc_playing():
    return run_audio_recognition()

# Entry point
while True:
    if acdc_playing():
        animate_leds()
    time.sleep(2)

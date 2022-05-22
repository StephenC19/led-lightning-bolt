import time
from ledStrip import *
sys.path.append(os.getcwd() + "/../audio-fingerprint-identifying-python/")
from recognizer import *

LED_COUNT = 300

def turn_on_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, [255, 0, 0])
    strip.stripShow()

def turn_off_leds(strip):
    for k in range(LED_COUNT):
        strip.setPixel(k, [0, 0, 0])
    strip.stripShow()

def animate_leds():
    l = LedStrip(LED_COUNT)

    # Blink
    turn_on_leds(l)
    time.sleep(0.2)
    turn_off_leds(l)
    time.sleep(1)

    # Blink
    turn_on_leds(l)
    time.sleep(0.5)
    turn_off_leds(l)
    time.sleep(2)

    # On
    turn_on_leds(l)
    time.sleep(120)
    turn_off_leds(l)
    time.sleep(0.5)
    turn_on_leds(l)
    time.sleep(0.2)
    turn_off_leds(l)


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

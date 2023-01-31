from recognizer import *
import requests

listen_length = 5
recognition_result = recognize(listen_length)

if recognition_result["match_found"] == True and recognition_result["accuracy"] > 40:
    r = requests.get(url = PI_URL)

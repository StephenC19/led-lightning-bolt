# LED Lightning Bolt
A LED lighting fixture which only lights up when AC/DC is playing. Using audio recognition, the script listens to ambient sound until it hears AC/DC, which will then trigger the lights to turn on. To see more detail how I built it and how it works [click here](https://youtu.be/E8X9B-ofx_M).

## Setup

### Components List
* [WS2812B LED strip](https://amzn.eu/d/2JC9MnN)
* [LED Power supply](https://amzn.eu/d/7orh0QY)
* [LED channel strip](https://amzn.eu/d/2Hze9Lk)
* Aluminium Sheet

### Build
[See how I put it together here!](https://youtu.be/E8X9B-ofx_M)

## Installation
For the audio recognition clone the repo and install the dependencies:
```
git clone git@github.com:StephenC19/audio-fingerprint-identifying-python.git
cd audio-fingerprint-identifying-python
git checkout recognizer-function
pip install -r requirements.txt
make clean reset
make tests
```

Install the library for controlling the LED strip `sudo pip install rpi_ws281x`.

As I can't share anyone's music online, you'll have to train the database yourself. You can do this by copying any mp3s into a folder in the audio recognition repo.

```
mkdir mp3
cd mp3
cp <path_to_mp3> ./
# repeat for more mp3s

# train database
make fingerprint-songs
```

For controling the LEDs you'll have to setup the values in config.py.

## Run
There's two ways of running it:
- Run it as a single script on a RaspberryPi using `sudo python led_lightning_bolt.py` however this could have dependency issues.
- Run as a LED server on a pi and the audio recogition on a separate machine. `sudo flask --app lightning_bolt_server run --host=0.0.0.0` on the pi and `make recognize-listen seconds=5`. First you'll have to set the local Pi IP url in the config on your other machine.

Built by Stephen Colfer

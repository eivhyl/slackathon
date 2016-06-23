import sys
from twython import TwythonStreamer
from gpiozero import LED
from time import sleep

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class PiStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print("Morsing: ", data['text'].encode('utf-8'), "\n")
            print()
            msg = data['text'].encode('utf-8')
            for char in msg.upper():
                if char in CODE:
                    for c in CODE[char]:
                        print(c)
                        led = LED(17)
                        if c == '-':
                            sleep(0.5)
                        else:
                            sleep(0.25)
                        led = None
                        sleep(0.25)
                else:
                    print(char)

    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()

if __name__ == "__main__":
    try:
        term_to_track = sys.argv[1]
    except:
        print('Usage: {} "term_to_track"'.format(sys.argv[0]))
        sys.exit()

    stream = PiStreamer(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    stream.statuses.filter(track=term_to_track)


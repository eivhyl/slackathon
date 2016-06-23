import sys
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))

# class MyStreamer(TwythonStreamer):
#     def on_success(self, data):
#         if 'text' in data:
#             username = data['user']['screen_name']
#             tweet = data['text']
#             print("@%s: %s" % (username, tweet))

if __name__ == "__main__":
    try:
        term_to_track = sys.argv[1]
    except:
        print('Usage: {} "term_to_track"'.format(sys.argv[0]))
        sys.exit()

    stream = MyStreamer(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    stream.statuses.filter(track=term_to_track)


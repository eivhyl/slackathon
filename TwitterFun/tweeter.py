import sys
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

if __name__ == "__main__":
    try:
        message = sys.argv[1] + " #unik_teknologihuset #stianskoffert"
    except:
        print('Usage: {} "message"'.format(sys.argv[0]))
        sys.exit()

    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    twitter.update_status(status=message)
    print("Tweeted: %s" % message)

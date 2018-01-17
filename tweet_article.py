import tweepy
from urllib.request import Request, urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import datetime

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'

try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
except tweepy.TweepError as e:
    print("Tweepy Error! ", e)
else:
    api = tweepy.API(auth)

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def post_atricle():
    req = Request("https://en.wikipedia.org/wiki/Special:Random")
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        url = response.geturl()

        soup = BeautifulSoup(response, 'html.parser')
        title = (soup.title.string).replace(' - Wikipedia', '')
        message = "Random Wikipedia article of the hour: {} {}".format(title, url)
        api.update_status(message)
        print("Update successful: {} at {}".format(message, time))

if __name__ == "__main__":
    post_atricle()

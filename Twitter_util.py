import twitter
from dotenv import load_dotenv, find_dotenv
import os
from os.path import join, dirname
import config

class TwitterUtil(object):
    auth = twitter.OAuth(consumer_key=config.API_KEY,
    consumer_secret=config.API_SECRET_KEY,
    token=config.ACCESS_TOKEN,
    token_secret=config.ACCESS_TOKEN_SECRET)

    def Post(self, text):
        tw = twitter.Twitter(auth=self.auth)
        tw.statuses.update(status=text)

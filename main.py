import requests
from bs4 import BeautifulSoup
import re
import datetime
import Content
import Twitter_util
from apscheduler.schedulers.blocking import BlockingScheduler

twische = BlockingScheduler()

@twische.scheduled_job('interval', minutes=120)
def main():
    Leo = Content.FortuneTelling("leo")
    LeoTweet = Twitter_util.TwitterUtil()
    print(Leo.Text())
    LeoTweet.Post(Leo.Text())

if __name__ == '__main__':
    twische.start()
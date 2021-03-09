import requests
from bs4 import BeautifulSoup
import re
import datetime
import Content
import Twitter_util
from apscheduler.schedulers.blocking import BlockingScheduler

twische = BlockingScheduler()

@twische.scheduled_job('interval', minutes=10)
def main():
    Leo = Content.FortuneTelling("leo")
    LeoTweet = Twitter_util.TwitterUtil()
    """
    print(Leo.WorkText())
    print(Leo.MoneyText())
    print(Leo.LoveText())
    print(Leo.TotalText())
    print(Leo.Text())
    """
    LeoTweet.Post(Leo.WorkText())
    LeoTweet.Post(Leo.MoneyText())
    LeoTweet.Post(Leo.LoveText())
    LeoTweet.Post(Leo.TotalText())
    LeoTweet.Post(Leo.Text())

if __name__ == '__main__':
    twische.start()
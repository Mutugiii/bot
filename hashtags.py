#!/usr/bin/env python3
import tweepy
import logging
import json
import csv
from config import create_api

logging.basicConfig(level=logging.INFO,filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Creating a stream Listener
class favRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        '''Process tweets of the stream'''
        logger.info(f'Processing the tweet id {tweet.id}')
        # Open CSV file and set up csv writer
        csv_file = open('csv/data.csv', 'a')
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception:
                logger.exception(f'Error while liking tweet of id {tweet.id}')
        if not tweet.retweeted:
            try:
                tweet.retweet()
                csv_writer.writerow([f'{tweet.id}',f'{tweet.user.name}', f'twitter.com/{tweet.user.screen_name}/status/{tweet.id}', f'{tweet.user.created_at}'])
            except Exception:
                logger.exception(f'Error while Retweeting tweet of id {tweet.id}')

        csv_file.close()
    def on_error(self, status_code):
        logger.error(status_code)
        # If stream exceeds the rate limit
        if status_code == 420:
            return False

def main():
    api = create_api()
    tweets_stream_listener = favRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_stream_listener)
    stream.filter(track=['#ikokazike', '#ikokazikenya','#ikokazi'])

if __name__ == '__main__':
    main()
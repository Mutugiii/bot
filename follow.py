#!/usr/bin/env python3
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO, filemode='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def follow_followers(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f'Following {follower.name}')
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        time.sleep(60)

if __name__ == '__main__':
    main()
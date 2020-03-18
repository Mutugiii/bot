import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logger.INFO, filename='logs/followlogs.log', filename='a', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def follow_followers():
    logger.info('Following Followers')
    for follower in tweepy.cursor(api.followers).items():
        if not follower.following:
            logger.info(f'Following {follower.name}')
            follower.follow()

def main():
    api = create_api()
    while True:
        follow_followers(api)
        time.sleep(30)

if __name__ == '__main__':
    main()
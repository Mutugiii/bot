import tweepy
import logging
from decouple import config
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename='logs/startlogs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s)
logger = logging.getLogger()

def create_api():
    consumer_key = config('API_KEY')
    consumer_secret = config('API_SECRET_KEY')
    access_token = config('ACCESS_TOKEN')
    access_token_secret = config('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception:
        logger.exception('Error Creating Api')

    now = datetime.now()
    current_time = now.strftime('%m/%d/%y, %H:%M:%S')
    logger.info('Api Created on {}'.format(current_time))
    return api
import tweepy
import logging
import json
from config import create_api

logging.basicConfig(level=logging.INFO,filename='logs/favRetweets.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class favRetweetListener(tweepy.StreamListener):
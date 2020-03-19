#!/usr/bin/env python
'''Script to delete all the tweets'''

import tweepy
from config import create_api

api = create_api()

for tweet in tweepy.Cursor(api.user_timeline).items():
    api.destroy_status(tweet.id)
print('Deleted!')
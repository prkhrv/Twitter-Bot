import tweepy as tp
import time
import os


# Genrate Your key at https://apps.twitter.com
consumer_key = #Your Consumer Key
consumer_secret = #Your Secret Key
access_token = #Your Token
access_secret = #Access Token



auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


os.chdir('models')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(10)

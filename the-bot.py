import tweepy as tp
import time
import os


consumer_key = 'IiTscAHmJK1oKHf3zfqKXGOyy'
consumer_secret = 'YqMejMv1oNO1HWGRo1w4jxp9TmnxYQfRlMBBFSAIhERtINWXG6'
access_token = '1045201757779849216-k9MYlZnkC8wFzagjomSp2lvfiYKdVs'
access_secret = 'sKe6CRF8vE2m3iu1Lz6fUko1PyymgfRkiZUyXUfq9Bpb3'



auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


os.chdir('models')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(10)

api_key = 'RO4TQ5PR60Yi2SUvm05k2q8xf'
api_secret_key = 'EiiEEu6yG7Fcn3cCHV3EedW7qkV2i2MS5MSPbH8PYp6aaaxzVP'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHP5HQEAAAAAtanFlh4cqQCjG4ul7VPsxunvM7s%3DqCl8RaoBEeDepjsEBpmm9h2MDLcMzp1DIqOvKz61kNH5tcuODh'

import tweepy
import pandas as pd
import time
auth = tweepy.OAuthHandler(api_key,api_secret_key)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

api = tweepy.API(auth, wait_on_rate_limit=True)
def get_related_tweet(the_query):
    #list to store tweets
    tweet_list = []
    count = 50

    try:
        for tweet in api.search(q=the_query,count = count):
            tweet_list.append(
                {'created_at':tweet.created_at,
                'tweet_id':tweet.id,
                'tweet_text':tweet.text}
            )
        return pd.DataFrame.from_dict(tweet_list)

    except BaseException as e:
        print(f'failed on status {str(e)}')
        time.sleep(3)

print('yoyo')
import tweepy

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if '@your_twitter_handle' in status.text:
            user_id = status.user.id_str
            user_name = status.user.screen_name
            tweet_text = status.text

            reply_text = f'@{user_name} Você me deu um @, {tweet_text}'
            api.update_status(status=reply_text, in_reply_to_status_id=status.id)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@your_twitter_handle'])


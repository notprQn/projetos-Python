import tweepy

auth = tweepy.OAuthHandler("hd7kZXbebFihV86jM72T8t8ZO", "t26k0rVj1U17qsxu4z80KLVzjDsTQfOYiN0KRclNIY6PJoHcew")
auth.set_access_token("1598827390456807424-ElFRkGFkecuITeMSR9c2fv9pNdhB6o", "q57fO9lIu8msQiAU4aWrHL3HLK65pAWk5bFCnaJ4uc4lb")

api = tweepy.API(auth)

# Define a function to handle incoming tweets
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Check if the tweet mentions you
        if '@NotprQn' in status.text:
            # Extract the user who mentioned you and the text of the tweet
            user_id = status.user.id_str
            user_name = status.user.screen_name
            tweet_text = status.text

            # Compose and send a reply tweet to the user who mentioned you
            reply_text = f'@{user_name} Thanks for mentioning me! Your tweet said: {tweet_text}'
            api.update_status(status=reply_text, in_reply_to_status_id=status.id)

# Set up stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# Start streaming and filter on tweets that mention you
myStream.filter(track=['@NotprQn'])


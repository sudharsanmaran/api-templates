import tweepy


class TwitterClient:
    def send_tweet(self,access_token,text):
        client = tweepy.Client(bearer_token=access_token)
        # tweet with duplicate content not alowed
        response = client.create_tweet(user_auth=False, text=text)
        # response = client.create_tweet(user_auth=False, text="Hello World!, Testing")
        print(response)
        return response.json()
    

class Client(TwitterClient):
    pass
        
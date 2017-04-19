class Storage(object):
    _tweets = []
    name = "Bojan"
    tweet_ajdi = 1
    tweet_count = 1
    tweet_default = {"id":tweet_ajdi,"name":name,"tweet":"This is the first tweet"}

    @classmethod
    def get_all_tweets(cls):
        if len(cls._tweets) < 1:
            cls._tweets.append(cls.tweet_default)
            return cls._tweets
        else:
            return cls._tweets

    @classmethod
    def get_single_tweet(cls,tweet_id):
        for tweet in cls._tweets:
            if tweet["id"] == tweet_id:
                return tweet
        else:
            return "There is no tweet with this id."

    @classmethod
    def saving_new_tweet(cls,tweet_body):
        cls.tweet_count += 1
        tweet = {"id":cls.tweet_count,"name":cls.name,"tweet":tweet_body}
        cls._tweets.append(tweet)

    @classmethod
    def delete_single_tweet(cls,tweet_id):
        index_tweets = 0
        for tweet in cls._tweets:
            if tweet["id"] == tweet_id:
                del cls._tweets[index_tweets]
                return "The tweet has been deleted."
            index_tweets += 1
        else:
            return "Nothing to delete."
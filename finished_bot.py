# eecs398-tweet-tree
# example tweet 1069598634310807558


# libraries

# TODO: import additional libraries for this project
from secret import *
from twarc import Twarc
from anytree import NodeMixin, RenderTree

# base class to hold tweets
class Tweet(NodeMixin):
    def __init__(self, message_in, user_in, id_in, parent_in=None):
        self.message = message_in
        self.user = user_in
        self.id = id_in
        self.parent=parent_in
    def __str__(self):
        return "@{}: {}".format(self.user, self.message)

# TODO: implement get_replies()
def get_replies(twarc_session, tweet_in, parent=None):
    # get reply iterator of tweet
    reply_iterator = t.replies(tweet_in)
    # try/catch - if there are no replies, the iterator will hit stop-iteration
    try:
        # there's replies!  cool.  get the top tweet, thats the current one (the parent)
        tweet = next(reply_iterator)
        # create a node in the tree
        node = Tweet(tweet['full_text'], tweet['user']['screen_name'], tweet_in['id'], parent)
        # loop through remaining replies
        for next_tweet in reply_iterator:
            # recursive leap of faith!
            get_replies(twarc_session, next_tweet, node)
    except StopIteration:
        # there's no replies, return
        return

    # this will return the root
    return node


# TODO: generate Twitter session
t = Twarc(consumer_key, consumer_secret, access_token_key, access_token_secret)

# TODO: ask user for tweet they would like turned into a tree
tweetID = input("Enter a Tweet ID: ")

myTweet = t.tweet(tweetID)

# TODO: get replies recursively
root = get_replies(t, myTweet)

for pre, fill, node in RenderTree(root):
    print(pre, node.__str__())

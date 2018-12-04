# eecs398-tweet-tree

# libraries

# TODO: import additional libraries for this project
from mysecret import *
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
def get_replies(twarc_session, tweetID_in, parent=None):
    reply_iterator = t.replies(tweetID_in)
    try:
        tweet = next(reply_iterator)
        node = Tweet(tweet['full_text'], tweet['user']['screen_name'], tweetID_in, parent)
        for next_tweet in reply_iterator:
            # recursive leap of faith!
            get_replies(twarc_session, next_tweet, node)
    except StopIteration:
        return
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

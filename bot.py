# eecs398-tweet-tree

# TODO: import libraries

# base class to hold tweets
class Tweet(NodeMixin):
    def __init__(self, message_in, user_in, id_in, parent_in = None):
        self.message = message_in
        self.user = user_in
        self.id = id_in
        self.parent = parent_in
    def __str__(self):
        return "@{}: {}".format(self.user, self.message)

# TODO: implement get_replies(), return root node
def get_replies(twarc_session, tweet, parent = None):
    return

# TODO: generate twarc Twitter session

# TODO: ask user for Tweet ID

# TODO: get tweet using twarc

# TODO: build tree using get_replies()

# TODO: call RenderTree()

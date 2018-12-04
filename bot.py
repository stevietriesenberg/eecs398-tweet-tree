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

# TODO: implement get_replies()
def get_replies(twarc_session, tweetID_in, parent = None):

# TODO: generate Twarc Twitter session

# TODO: ask user for Tweet ID

# TODO: get tweet using Twarc

# TODO: get replies recursively and build tree using get_replies()

# TODO: print tree
for pre, fill, node in RenderTree(root):
    print(pre, node.__str__())

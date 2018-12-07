# eecs398-tweet-tree
Starter code used for live demo of integrating the Twitter API and Python for EECS 398 Fall 2018 at University of Michigan, Ann Arbor.
Last semester's demo on graphing hashtag usage can be found [here](https://github.com/stevietriesenberg/eecs398-python-twitter)

## Requirements

### [twarc](https://github.com/DocNow/twarc)

```
$ pip3 install twarc
```
- created specifically to pull data from Twitter

- handles authentication in one line

- not very well-documented, but it has the reply-searching functionality we're looking for

### [anytree](https://anytree.readthedocs.io/en/latest/)

```
pip3 install anytree
```
- simple and easy to use

- gives node functionality to any user-defined class

- builds AND renders trees


## What's included?

#### ``bot.py`` contains starter code for the Python program

#### ``secret.py`` will hold your API keys and tokens

- you want to keep your API keys secret, which is why they are placed in a separate file from your program.

- if you choose to put your project on GitHub, DO NOT commit ``secret.py``

## How to Generate Twitter API Keys and Tokens

### Go to [https://apps.twitter.com](https://apps.twitter.com)

#### NOTE: You will need a Twitter account from this point on.

- sign into Twitter, then click "Create New App" in the upper right

- fill out the name, description, and website for your application.  Check the "Developer Agreement" box and finish creating your app!

- under the name of your application, find and click the "Keys and Access Tokens" tab

### Consumer Keys

- located under Application Settings

- copy and paste these keys into ``secret.py``

### Access Tokens

- scroll down and click "Authorize my Application"

- located under "Your Access Token"

- copy and paste these keys into ``secret.py``


### TODO: import libraries

- ``from twarc import Twarc``

- ``from anytree import NodeMixin, RenderTree``

- ``from secret import *``

### TODO: create a new Twitter session

- check out "Using as a Library" in the [twarc README](https://github.com/DocNow/twarc)

- use keys/tokens from ``secret.py`` to create the session

### TODO: user input

- ask the user (you) for a Tweet ID

### TODO: get the user's requested Tweet

- use your twarc session for this

- the Tweet will be represented as a large dictionary

### TODO: implement get_replies() and call it to build the tree

- we have to be resourceful here - there's no documentation on twarc's reply functionality, but we can look at twarc's [test file](https://github.com/DocNow/twarc/blob/master/test_twarc.py) on GitHub to figure out how to use it

- "take the recursive leap of faith!"

### TODO: display the tree

- use anytree's ``RenderTree`` functionality

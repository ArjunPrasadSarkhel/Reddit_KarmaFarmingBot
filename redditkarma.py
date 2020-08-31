import praw
import time
from random import choice

reddit = praw.Reddit(user_agent='',
                  client_id='',
                  client_secret='',
                  username='',
                  password='')

while True:
    try:
      with open("lines.txt") as f:
            lines = [l.rstrip() for l in f]

      for comment in reddit.subreddit("").stream.comments(skip_existing=True):
        if comment.author.name != "":
            comment.reply(choice(lines))
            comment.upvote()
            reply = comment.reply
            
    except Exception as e:
        print(e)
        time.sleep(60)
        

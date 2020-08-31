import praw
import time
from random import choice

reddit = praw.Reddit(user_agent='test-script',
                  client_id='En5dWl9v8IhrQA',
                  client_secret='m7GxwQGjBK8GIjHK4b5s1275Yi0',
                  username='HeavyIncomeTax',
                  password='maaaaice623')

while True:
    try:
      with open("lines.txt") as f:
            lines = [l.rstrip() for l in f]

      for comment in reddit.subreddit("FreeKarma4U").stream.comments(skip_existing=True):
        if comment.author.name != "HeavyIncomeTax":
            comment.reply(choice(lines))
            comment.upvote()
            reply = comment.reply
            
    except Exception as e:
        print(e)
        time.sleep(60)
        

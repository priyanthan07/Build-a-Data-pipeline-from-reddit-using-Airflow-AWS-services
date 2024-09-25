import praw
from praw import Reddit
import sys
import numpy as np
import pandas as pd

from util.constants import POST_FIELDS



def connect_reddit(client_id, secret_id, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(
            client_id = client_id,
            client_secret = secret_id,
            user_agent = user_agent
        )
        print("connected to reddit server")
        return reddit
    
    except Exception as e:
        print(e)
        sys.exit(1)
        

def extract_posts(reddit_instance: Reddit, subreddit:str, time_filter:str, limit:None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)
    
    post_lists = []
    
    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)
    
        print(post)
        
    return post_lists

def transform_data(data : pd.DataFrame):
    data['created_utc'] = pd.to_datetime(data['created_utc'], unit='s')
    data['over_18'] = data['over_18'] = np.where((data['over_18'] == True), True, False)
    data['author'] = data['author'].astype(str)
    edited_mode = data['edited'].mode()
    data['edited'] = np.where(data['edited'].isin([True, False]),
                                 data['edited'], edited_mode).astype(bool)
    data['num_comments'] = data['num_comments'].astype(int)
    data['score'] = data['score'].astype(int)
    data['title'] = data['title'].astype(str)

    return data
    
def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)
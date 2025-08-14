import time
import pandas as pd
from datetime import datetime, timezone

def stream_comments_to_dataframe(reddit, subreddit_name, duration_seconds=360, skip_existing=True):
    """
    Stream comments from a subreddit and save them into a pandas DataFrame.

    Args:
        reddit (praw.Reddit): An authenticated PRAW Reddit instance.
        subreddit_name (str): Name of the subreddit to stream comments from.
        duration_seconds (int, optional): Duration of the streaming in seconds. Default is 360.
        skip_existing (bool, optional): Whether to skip existing comments when streaming. Default is True.

    Returns:
        pd.DataFrame: DataFrame with two columns:
            - 'datetime': UTC timestamp of the comment
            - 'text': Text content of the comment
    """
    subreddit = reddit.subreddit(subreddit_name)
    comments_list = []
    start_time = time.time()
    
    print(f"Start streaming from r/{subreddit_name}...")
    
    for comment in subreddit.stream.comments(skip_existing=skip_existing):
        dt = datetime.fromtimestamp(comment.created_utc, tz=timezone.utc)
        comments_list.append({"datetime": dt, "text": comment.body})
        
        # Stop after the duration
        if time.time() - start_time > duration_seconds:
            print("Stop streaming!")
            break
    
    df = pd.DataFrame(comments_list)
    return df



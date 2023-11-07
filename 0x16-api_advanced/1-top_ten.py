#!/usr/bin/python3
"""
Define a method that queries the Reddit API
and print titles of posts.
"""
from requests import get


def top_ten(subreddit):
    """
    Fetch the titles of the first 10 hot
    posts for the given subreddit.

    Parameters
    subreddit : string
        The subreddit to query
    """
    with get(f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9",
             allow_redirects=False) as res:
        if (res.status_code == 200):
            for item in res.json()["data"]["children"]:
                print(item["data"]["title"])
        else:
            print("None")

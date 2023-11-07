#!/usr/bin/python3
"""
Define a function that returns a list
containing the titles of all hot articles
for a given subreddit.
"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """
    Return a list containing the titles of
    all hot articles for a subreddit.

    Parameters
    subreddit : string
        The subreddit to query

    hot_list : list
        A list of titles for all hot
        articles

    after : string, optional
        The parameter used for pagination.
        The default value is an empty string,
        denoting the very first request (first
        page)

    Return
        A list of titles for all hot
        articles
    """
    param = {"after": after}
    with get(f"https://www.reddit.com/r/{subreddit}/hot.json",
             params=param) as res:
        if (res.status_code == 200):
            for item in res.json()["data"]["children"]:
                hot_list.append(item["data"]["title"])

            after = res.json()["data"]["after"]

            if (after is not None):
                return (recurse(subreddit, hot_list, after))

            return (hot_list)

#!/usr/bin/python3
"""
Define a function that parses the titles for
hot articles and prints a sorted count of
the given keywords.
"""
from requests import get


def count_words(subreddit, word_list):
    """
    Parse the title for articles for the given
    subreddit and keywords and print the count
    for each keyword.

    Parameters
    subreddit : string
        The subreddit to query

    word_list : list
        A list containing the keywords to
        search for
    """
    results = parse(subreddit, word_list)
    for key, val in results:
        print(f"{key}: {value}")

def parse(subreddit, word_list, after="", results={}):
    """
    Parse the title for articles for the given
    subreddit and keywords and print the count
    for each keyword.

    Parameters
    subreddit : string
        The subreddit to query

    word_list : list
        A list containing the keywords to
        search for

    after : string, optional
        The parameter used for pagination.
        The default value is an empty string,
        denoting the very first request (first
        page)

    results : dict, optional
        The count of the given keywords
    """
    param = {"after": after}
    should_add = False

    with get(f"https://www.reddit.com/r/{subreddit}/hot.json",
             params=param) as response:
        if (response.status_code == 200):
            res = response.json()
            for item in res["data"]["children"]:
                for keyword in keywords:
                    if (keyword in item["data"]["title"]):
                        should_add = True
                        break
                if (should_add):
                    value = results.get(keyword)
                    results[keyword] = 1 if not value else value + 1

            after = res["data"]["after"]

            if (after):
                return (parse(subreddit, word_list, after, results))
            return (results)

#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for given subreddit
    """
    try:
        url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
        header = {'User-Agent': ""}
        req = requests.get(url, headers=header)
        sub = req.json()['data'].get('subscribers', 0)
        return sub
    except:
        return 0

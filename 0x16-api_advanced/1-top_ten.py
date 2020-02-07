#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Return first 10 hot posts for given subreddit
    """
    try:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
        header = {'User-Agent': ""}
        req = requests.get(url, headers=header)
        for post in req.json()['data'].get('children'):
            print(post['data'].get('title'))
    except:
        print('None')

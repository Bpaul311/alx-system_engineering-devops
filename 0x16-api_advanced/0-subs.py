#!/usr/bin/python3
"""
Script that returns number of subs of a given subreddit
"""
import requests 

def number_of_subscribers(subreddit):
    """returns the number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "RedditScaper"}
    response = requests.get(url, headers= headers, allow_redirects = False)

    if response.status_code == 200:
        user_data = response.json()
        subs = user['user_data']['subscribers']
        return subs
    else:
        return 0

#!/usr/bin/python3
""" Queries the Reddit API and prints hot posts for a given subreddit"""

import requests

def top_ten(subreddit):
    """ Prints the first 10 hot posts for the given subreddit """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    result = response.json().get("data")
    [print(c.get("data").get("title"))for c in results.get("children")]

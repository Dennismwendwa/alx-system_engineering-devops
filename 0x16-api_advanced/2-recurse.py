#!/usr/bin/python3
"""This script uses recursition to paginate api responses"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This function sends get request"""
    if hot_list is None:
        hot_list = []

    url = (
           f"https://www.reddit.com/r/{subreddit}/hot.json?"
           f"limit=10&after={after}"
           )

    headers = {"User-Agent": "MyBot"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()

        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

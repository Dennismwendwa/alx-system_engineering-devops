#!/usr/bin/python3
"""
This script sends get request to reddit api and
counts the titles return
"""
import requests


def top_ten(subreddit):
    """
    This function send get request to reddit api
    """
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            title = post["data"]["title"]
            print(f"{title}")
    else:
        print(None)

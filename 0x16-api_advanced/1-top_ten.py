#!/usr/bin/python3
"""sending request to reddit api"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "MyBot"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        posts = data["data"]["children"]

        for k, post in enumerate(posts[:10]):
            title = post["data"]["title"]
            print(f"{title}")

    else:
        print(None)

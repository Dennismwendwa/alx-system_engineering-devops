#!/usr/bin/python3
"""this script sends request to reddit api"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "MyBot"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        sunscribers = data["data"]["subscribers"]
        return sunscribers
    else:
        return 0

#!/usr/bin/python3
"""THis script sends get request to apis"""
import requests


def count_words(subreddit, word_list, new_list=[], after=None):
    """This script prints the count of words"""
    headers = {"User-Agent": "MyBot"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    response = requests.get(url, headers=headers)

    if after is None:
        word_list = [w.lower() for w in word_list]

    if response.status_code == 200:
        data = response.json()["data"]
        afr = data["after"]
        posts = data["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in title.split(" "):
                if word in word_list:
                    new_list.append(word)
        if afr is not None:
            count_words(subreddit, word_list, new_list, afr)
        else:
            every = {}
            for w in new_list:
                if w.lower() in every.keys():
                    every[w.lower()] += 1
                else:
                    every[w.lower()] = 1
            for k, v in sorted(
                               every.items(),
                               key=lambda item: item[1],
                               reverse=True
                               ):
                print(f"{k}: {v}")

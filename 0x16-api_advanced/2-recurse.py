#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top hot posts of a subreddit
"""
import requests


def add_title(lists, posts):
    """Adds posts to a list"""
    if len(posts) == 0:
        return
    lists.append(posts[0]['data']['title'])
    posts.pop(0)
    add_title(lists, posts)


def recurse(subreddit, hot_list=[], after=None):
    """Queries Reddit API"""
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }
    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    res = response.json()
    after = res['data']['after']
    add_title(hot_list, res['data']['children'])
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)

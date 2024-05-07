#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def add_to_list(hot_list, hot_posts):
    """Adds titles to a list """
    if len(hot_posts) == 0:
        return

    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_to_list(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after,
    }

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    res_json = response.json()
    hot_posts = res_json['data']['children']

    add_to_list(hot_list, hot_posts)
    after = res_json['data']['after']

    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)

#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """Returns top ten posts"""
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    res_json = response.json()
    hot_posts = res_json['data']['children']
    if response.status_code != 200:
        print("None")
        return
    if len(hot_posts) == 0:
        print("None")
    else:
        for post in hot_posts:
            print(post['data']['title'])

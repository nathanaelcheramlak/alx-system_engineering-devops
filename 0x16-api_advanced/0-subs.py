#!/usr/bin/python3
import requests
import sys

def number_of_subscribers(subreddit):
    """Returns the number of subscribers of a subreddit"""

    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers,  allow_redirects=False)
    res = response.json()

    if response.status_code != 200:
        return 0

    if 'data' in res:
        return res['data']['subscribers']
    return 0


if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
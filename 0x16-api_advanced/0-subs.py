#!/usr/bin/python3
"""number_of_subscribers(subreddit)"""


def get_subreddit_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")

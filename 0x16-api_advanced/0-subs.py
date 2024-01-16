#!/usr/bin/python
"""
Reddit API - How many subs?
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit

    Args:
        subreddit (str): The subreddit name

    Returns:
        int: The number of subscribers, or 0 if the aubreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'Termux:0x16.api-avanced (by Jonaben)'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0


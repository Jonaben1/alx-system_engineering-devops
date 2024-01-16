#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after="", counts=None):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json().get("data")
        titles = [post["data"]["title"] for post in data["children"]]

        for title in titles:
            for word in word_list:
                keyword = word.lower()
                title_lower = title.lower()
                
                if title_lower.count(keyword) > 0:
                    counts[keyword] = counts.get(keyword, 0) + title_lower.count(keyword)

        after = data.get("after")
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)

    except requests.RequestException as e:
        print(f"Error: {e}")

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        print(f"{word}: {count}")

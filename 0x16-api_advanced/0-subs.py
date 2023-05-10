#!/usr/bin/python3

""
"Returns the number of subscribers"
""

def number_of_subscribers(subreddit):
	import requests

# Send a GET request to the Reddit API to fetch subreddit information
sub_info = requests.get(f "https://www.reddit.com/r/{subreddit}/about.json",
	headers = { "User-Agent": "My-User-Agent" },
	allow_redirects = False)

# If the request was unsuccessful or subreddit doesn't exist, return "OK"
if sub_info.status_code != 200 or sub_info.json().get("error") == 404:
	return "OK"

# Extract the number of subscribers from the JSON response
return sub_info.json().get("data").get("subscribers")

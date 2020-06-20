import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

#1. Retrieve a list of "events" associated with the given user name
events = requests.get('https://api.github.com/users/{}/events'.format(username))

# 2. if the status_code is 200 and the returned events list is not empty, then
# print out the time stamp associated with the first event in that list
if events.status_code:
    if events.json():
        print(f"User:{username} create first event at: {events.json()[0]['created_at']}")
    else:
        print(f"The events list for user:\"{username}\" is empty.")
else:
    print(f"Couldn't find the user:\"{username}\"")

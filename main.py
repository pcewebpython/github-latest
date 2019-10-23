import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.
    print("Input User Name:")
    user_id = input()
    response = requests.get("https://api.github.com/users/{}/events".format(user_id))
    event = response.json()
    print(event[0]['created_at'])
import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    # print("COMPLETE THE TODOs")
    
    api_url = 'https://api.github.com'
    try:
        events = requests.get(f'{api_url}/users/{username}/events')
        first = events.json()[0]['created_at']
    except:
        first = None

    if first:
        print(f"First event for user {username} was at {first}")
    else:
        print("Unable to retrieve timestamp for user.")
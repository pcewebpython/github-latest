import sys
import json

import requests

# Use Like python githubber.py JASchilz
def get_users_events(username):
    """returns a list of events for user from github"""
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    return response.json()
# (or another user name)


if __name__ == "__main__":
    username = sys.argv[1]
    events = get_users_events(username)

    print(events[0]['created_at'])

    



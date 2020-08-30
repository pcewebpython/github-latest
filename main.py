import sys

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    user_info = requests.get(url=f"https://api.github.com/users/{username}").json()
    events_url = user_info['events_url'].strip("{/privacy}")
    events = requests.get(url=events_url).json()
    print(events[0]["created_at"])

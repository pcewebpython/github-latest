# Stella Kim
# Activity 6: Github API

import sys
import json
import requests


if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get(
        'https://api.github.com/users/{}/events'.format(username))
    events = json.loads(response.content)
    print(events)  # events associated with given username
    print(events[0]['created_at'])  # first event timestamp in list

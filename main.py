import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    root = 'https://api.github.com'
    r = requests.get(root + '/users/{}/events'.format(username))
    events_list = r.json()


    print("User {}: last event at {}".format(username, events_list[0]['created_at']))
    



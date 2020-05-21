# main.py

import sys
import json
import requests

# Use like python main.py username
# Ex. python main.py ramr

if __name__ == "__main__":
    username = sys.argv[1]
    # Retrieve a list of "events" associated with the given user name
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)

    # Print out the time stamp associated with the first event in that list
    print(events[0]['created_at'])

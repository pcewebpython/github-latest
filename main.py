import sys
import json

import requests

if __name__ == "__main__":
    act_user = True
    
    while act_user:
        username = input('Please provide username for event retrival: ')
        response = requests.get("https://api.github.com/users/{user}/events/public".format(user=username))
        try:
            timestamp = response.json()[0]['created_at']
            print('First Event in List Created at: ', timestamp)
            act_user = False
        except IndexError:
            print('Please confirm User Id is accurate')

    print("COMPLETE THE TODOs -- Thank You")

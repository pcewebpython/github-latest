import sys
import json
import requests

# https://api.github.com/
# https://api.github.com/feeds


def get_response(usr):
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    events = json.loads(response.content)
    # print(events)
    print(events[0]['created_at'])


if __name__ == "__main__":
    username = sys.argv[1]
    # username = 'geekwriter2'
    get_response(username)






    



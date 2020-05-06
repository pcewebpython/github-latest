import sys
import json

import requests

def get_user_info(user):
    response = requests.get(f"https://api.github.com/users/{user}/events")
    event_data = json.loads(response.content)
    latest_event = f"{event_data[0]['actor']['login']}'s latest event "\
                   f"was a {event_data[0]['type']}, which occurred at "\
                   f"{event_data[0]['created_at']}"

    return latest_event

if __name__ == "__main__":
    username = sys.argv[1]
    result = get_user_info(username)
    print(result)

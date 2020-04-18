import sys
import json

import requests

if __name__ == "__main__":
    # CLI: python main.py username
    username = sys.argv[1]
    response = requests.get(f"https://api.github.com/users/{username}/events")

    print(f"The latest GitHub event for {username} occurred at: " +
    response.json()[0]['created_at'])

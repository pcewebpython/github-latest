import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    #***MMM
    #username = "mmanc125uw"
    
    
    # Done:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    
    ###diag
    ### ***MMM for response result see https://api.github.com/users/username/events 
    ###          ex  https://api.github.com/users/mmanc125uw/events 
    #print(response.content)
    #dict = response.json()[0]
    #for key, value in dict.items():
    #    print(f"diag  key = -{key}- value = -{value}-")
    #print(f" resp json [0] keys = {response.json()[0].keys()}")
    ###
    
    events = json.loads(response.content)

    print(events[0]['created_at'])
    


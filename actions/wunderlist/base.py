from ..base import Action
import requests
import json
import config

GET_LISTS_URL = "https://a.wunderlist.com/api/v1/lists"
CREATE_TASK_URL = "https://a.wunderlist.com/api/v1/tasks"

# Superclass that handles common client setup for actual Wunderlist actions
class WunderlistAction(Action):
    def __init__(self):
        super(WunderlistAction, self).__init__()
        self.client = WunderlistClient(config.WUNDERLIST_CLIENT_ID, config.WUNDERLIST_ACCESS_TOKEN)

# Wunderlist REST client
class WunderlistClient():
    def __init__(self, client_id, access_token):
        self.headers = {
            "Content-Type": "application/json",
            "X-Access-Token": access_token,
            "X-Client-ID": client_id
        }
        
    def get_lists(self):
        r = requests.get(GET_LISTS_URL, headers=self.headers)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    def get_list_id(self, list_name):
        lists = filter(lambda x: x["title"] == list_name, self.get_lists())
        # TODO: throw a real exception if list is not found, instead of index out of bounds
        return lists[0]["id"]
    
    def create_task(self, list_name, title):
        payload = {
            "list_id": self.get_list_id(list_name),
            "title": title
        }
        r = requests.post(CREATE_TASK_URL, data=json.dumps(payload), headers=self.headers)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
import requests
import json

class HueClient():
    def __init__(self, ip, user):
        self.lights_url = "https://%(ip)/api/%(user)/lights" % {"ip": ip, "user": user} 
        
    def get_lights(self):
        r = requests.get(GET_LISTS_URL, headers=self.headers)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    def get_light_state(self, light_name):
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
import requests
import json

class HueClient():
    def __init__(self, ip, user):
        self.groups_url = "http://" + ip + "/api/" + user + "/groups/"
        
    def get_groups(self):
        r = requests.get(self.groups_url)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    def get_group_id(self, group_name):
        groups = filter(lambda x: x[1]["name"] == group_name, self.get_groups().items())
        # TODO: throw a real exception if list is not found, instead of index out of bounds
        return groups[0][0]
       
    def get_group_info(self, group_id):
        url = self.groups_url + str(group_id)
        r = requests.get(url)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    def toggle_group(self, group_name):
        group_id = self.get_group_id(group_name)
        url = self.groups_url + str(group_id) + "/action"
        payload = {"on": False if self.get_group_info(group_id)["state"]["any_on"] else True}
        r = requests.put(url, data=json.dumps(payload))
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
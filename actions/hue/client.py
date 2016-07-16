import requests
import json

class HueClient():
    def __init__(self, ip, user):
        self.base_url = "http://" + ip + "/api/" + user
        self.groups_url = self.base_url + "/groups/"
        self.scenes_url = self.base_url + "/scenes/"
        
    def toggle_group(self, group_name):
        group_id = self.get_group_id(group_name)
        is_on = not self.get_group_info(group_id)["state"]["any_on"]
        return self.set_state(group_id, on=is_on)
    
    def set_scene(self, group_name, scene_name):
        group_id = self.get_group_id(group_name)
        scene_id = self.get_scene_id(scene_name)
        return self.set_state(group_id, scene=scene_id)
    
    def get_groups(self):
        return self.get_url(self.groups_url)
    
    def get_group_id(self, group_name):
        groups = self.get_groups()
        named_group = filter(lambda x: groups[x]["name"] == group_name, groups.keys())
        return named_group[0] if named_group else None
       
    def get_group_info(self, group_id):
        return self.get_url(self.groups_url + str(group_id))
    
    def get_scenes(self):    
        return self.get_url(self.scenes_url)
    
    def get_scene_id(self, scene_name):
        scenes = self.get_scenes()
        named_scene = filter(lambda x: scenes[x]["name"] == scene_name, scenes.keys())
        return named_scene[0] if named_scene else None
        
    def set_state(self, group_id, **kwargs):
        url = self.groups_url + str(group_id) + "/action"
        r = requests.put(url, data=json.dumps(kwargs))
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    def get_url(self, url):
        r = requests.get(url)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
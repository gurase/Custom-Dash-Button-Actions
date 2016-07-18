from ..base import Action
import requests
import json
import config

# Superclass that handles common client setup for actual Philips Hue actions
class HueAction(Action):
    def __init__(self):
        super(HueAction, self).__init__()
        self.client = HueClient(config.HUE_IP, config.HUE_USER)

# Philips Hue REST client
class HueClient():
    def __init__(self, ip, user):
        self.base_url = "http://" + ip + "/api/" + user
        self.groups_url = self.base_url + "/groups/"
        self.scenes_url = self.base_url + "/scenes/"
        
    def toggle_group(self, group_name):
        group_id = self.get_group_id(group_name)
        is_on = not self.get_group(group_id)["state"]["any_on"]
        return self.set_state(group_id, on=is_on)
    
    def set_scene(self, group_name, scene_name):
        group_id = self.get_group_id(group_name)
        scene_id = self.get_scene_id(group_id, scene_name)
        return self.set_state(group_id, scene=scene_id)
    
    def color_cycle(self, group_name):
        group_id = self.get_group_id(group_name)
        return self.set_state(group_id, on=True, effect="colorloop")
    
    def get_groups(self):
        return self.get_url(self.groups_url)
    
    def get_group_id(self, group_name):
        groups = self.get_groups()
        named_group = filter(lambda x: groups[x]["name"] == group_name, groups.keys())
        return named_group[0] if named_group else None
       
    def get_group(self, group_id):
        return self.get_url(self.groups_url + str(group_id))
    
    def get_scenes(self):
        return self.get_url(self.scenes_url)
    
    # get first scene that contains only the lights in the given group
    def get_scene_id(self, group_id, scene_name):
        scenes = self.get_scenes()
        group = self.get_group(group_id)
        named_scene = filter(lambda x: scenes[x]["name"] == scene_name and set(scenes[x]["lights"]) == set(group["lights"]), scenes.keys())
        return named_scene[0] if named_scene else None
        
    def set_state(self, group_id, **kwargs):
        url = self.groups_url + str(group_id) + "/action"
        r = requests.put(url, data=json.dumps(kwargs))
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
    
    # TODO: Move this out into a common area
    def get_url(self, url):
        r = requests.get(url)
        if (r.status_code == requests.codes.ok):
            return r.json()
        else:
            r.raise_for_status()
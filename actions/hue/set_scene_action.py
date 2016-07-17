from ..base import Action
from .client import HueClient
import config

class SetSceneAction(Action):
    def __init__(self, group_name, scene_name):
        self.group_name = group_name
        self.scene_name = scene_name
    def execute(self):
        client = HueClient(config.HUE_IP, config.HUE_USER)
        client.set_scene(self.group_name, self.scene_name)
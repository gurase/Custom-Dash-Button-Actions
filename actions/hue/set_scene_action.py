from .base import HueAction
import config

class SetSceneAction(HueAction):
    def __init__(self, group_name, scene_name):
        super(SetSceneAction, self).__init__()
        self.group_name = group_name
        self.scene_name = scene_name
        
    def execute(self):
        self.client.set_scene(self.group_name, self.scene_name)
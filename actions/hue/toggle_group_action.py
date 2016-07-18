from .base import HueAction
import config

class ToggleGroupAction(HueAction):
    def __init__(self, group_name):
        super(ToggleGroupAction, self).__init__()
        self.group_name = group_name
        
    def execute(self):
        self.client.toggle_group(self.group_name)
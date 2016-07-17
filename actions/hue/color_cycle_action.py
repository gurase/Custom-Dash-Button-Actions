from .base import HueAction
import config

class ColorCycleAction(HueAction):
    def __init__(self, group_name):
        super(ColorCycleAction, self).__init__()
        self.group_name = group_name
        
    def execute(self):
        self.client.color_cycle(self.group_name)
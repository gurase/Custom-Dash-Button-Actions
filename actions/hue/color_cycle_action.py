from ..base import Action
from .client import HueClient
import config

class ColorCycleAction(Action):
    def __init__(self, group_name):
        self.group_name = group_name
    def execute(self):
        client = HueClient(config.HUE_IP, config.HUE_USER)
        client.color_cycle(self.group_name)
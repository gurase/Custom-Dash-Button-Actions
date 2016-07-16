from ..base import Action
from .client import HueClient
import config

class ToggleGroupAction(Action):
    def __init__(self, group_name):
        self.group_name = group_name
    def execute(self):
        client = HueClient(config.IP, config.USER)
        client.toggle_group(self.group_name)
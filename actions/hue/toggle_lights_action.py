from ..base import Action
from .client import HueClient
import config

class ToggleLightsAction(Action):
    def __init__(self, *args):
        self.lights = args
    def execute(self):
        client = HueClient(config.HUE_IP, config.HUE_USER)
        client.toggle_lights(lights)
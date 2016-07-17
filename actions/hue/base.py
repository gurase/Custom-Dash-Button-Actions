from ..base import Action
from .client import HueClient
import config

class HueAction(Action):
    def __init__(self):
        super(HueAction, self).__init__()
        self.client = HueClient(config.HUE_IP, config.HUE_USER)
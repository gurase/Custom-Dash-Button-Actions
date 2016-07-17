from ..base import Action
from .client import WunderlistClient
import config

class WunderlistAction(Action):
    def __init__(self):
        super(WunderlistAction, self).__init__()
        self.client = WunderlistClient(config.WUNDERLIST_CLIENT_ID, config.WUNDERLIST_ACCESS_TOKEN)
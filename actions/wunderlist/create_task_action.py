from ..base import Action
from .client import WunderlistClient
import config

class CreateTaskAction(Action):
    def __init__(self, list_name, task_title):
        self.list_name = list_name
        self.task_title = task_title
    def execute(self):
        client = WunderlistClient(config.WUNDERLIST_CLIENT_ID, config.WUNDERLIST_ACCESS_TOKEN)
        client.create_task(self.list_name, self.task_title)
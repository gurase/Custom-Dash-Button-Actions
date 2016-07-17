from .base import WunderlistAction
import config

class CreateTaskAction(WunderlistAction):
    def __init__(self, list_name, task_title):
        super(CreateTaskAction, self).__init__()
        self.list_name = list_name
        self.task_title = task_title
    def execute(self):
        self.client.create_task(self.list_name, self.task_title)
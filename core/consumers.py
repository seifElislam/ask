"""

"""
import json
from channels.generic.websocket import WebsocketConsumer

online_users = []


class Consumer(WebsocketConsumer):
    def connect(self):
        if self.scope.get('user'):
            online_users.append(1)
            self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        self.send(text_data=json.dumps({
            'msg': message
        }))

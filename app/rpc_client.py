import json
import pika

class RpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='krabbitmq'))

        self.channel = self.connection.channel()

    def call(self, body):
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=json.dumps(body))
        print('Message sended')
        return 'Sended'

import json
import pika
print('now not connected')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='krabbitmq'))
print('connected')
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    response = json.loads(body)
    print('hello')
    print(response)


channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

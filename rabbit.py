import pika
import time
import socket
pingcounter = 0
isreachable = False
while isreachable is False and pingcounter < 5:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('rabbitmq', 5672))
        isreachable = True
    except socket.error as e:
        time.sleep(2)
        pingcounter += 1
    s.close()
if isreachable:
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                         routing_key='hello',
                          body='Hello World!')
    print (" [x] Sent 'Hello World!'")
    connection.close()

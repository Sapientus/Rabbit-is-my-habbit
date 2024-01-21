import pika
from models import *
import connection

User.drop_collection()  # To make sure previous fake users are deleted
user_input = input("Enter users` amount: ")
generator(int(user_input))

users = User.objects(logic_field=False)


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connect = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connect.channel()

    channel.queue_declare(queue="sending_users")

    for us in users:
        channel.basic_publish(
            exchange="", routing_key="sending_users", body=str(us.id).encode()
        )
        print(f" [x] Sent {str(us.id)}!")
    connect.close()


main()

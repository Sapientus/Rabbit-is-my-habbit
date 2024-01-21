import pika
import sys
from models import *
import connection


def get_user(user_id):
    try:
        user = User.objects.get(id=user_id.decode())
        user.logic_field = True
        user.save()
    except DoesNotExist:
        pass


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connect = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connect.channel()

    channel.queue_declare(queue="sending_users")

    def callbak(ch, method, properties, body):
        get_user(body)
        print(f"User: {body.decode()} was done")

    channel.basic_consume(queue="sending_users", on_message_callback=callbak)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)

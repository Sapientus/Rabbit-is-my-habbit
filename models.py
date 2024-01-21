from mongoengine import *
from faker import Faker
from random import randint

faker = Faker()


class User(Document):
    fullname = StringField(max_length=50, required=True)
    email = StringField(max_length=150, required=True)
    age = IntField()
    logic_field = BooleanField(default=False)
    meta = {"collection": "users"}


def generator(amount):
    for _ in range(amount):
        user = User(
            fullname=faker.name(),
            email=faker.email(),
            age=randint(14, 90),
        )
        user.save()

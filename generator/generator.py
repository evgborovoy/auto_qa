import random

from faker import Faker
import os
from data.data import Person

fake = Faker("ru_RU")


def generated_person():
    yield Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=fake.random_int(18, 80),
        department=fake.job(),
        salary=fake.random_int(1000, 12000, 50),
        full_name=fake.first_name() + " " + fake.last_name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
        phone=random.randint(1000000000, 9999999999)
    )


def generate_file():
    path = rf"{os.getcwd()}/media/testfile.txt"
    file = open(path, "w+")
    file.write(f"Some Text {random.randint(1, 10)}")
    file.close()
    return file.name, path

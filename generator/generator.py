from faker import Faker

from data.data import Person

fake = Faker("ru_RU")


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
    )

from faker import Faker

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
    )

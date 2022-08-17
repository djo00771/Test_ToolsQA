import random

from data.data import Person
from faker import Faker


faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=faker_ru.random.randint(20, 40),
        salary=faker_ru.random.randint(50, 100000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_file():
    path = rf'C:\Users\zay-e\PycharmProjects\Test_ToolsQA\filename{random.randint(0, 500)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 500)}')
    file.close()
    return file.name, path

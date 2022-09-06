import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')


# Faker.seed()


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
        mobile=faker_ru.msisdn(),
        subject='English'
    )


def generated_file_for_test_elements():
    path = rf'C:\Users\zay-e\PycharmProjects\Test_ToolsQA\filename{random.randint(0, 500)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 500)}')
    file.close()
    return file.name, path


def generated_file_for_test_form():
    path = rf'C:\Users\zay-e\PycharmProjects\ToolsQA\test{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'HelloWorld{random.randint(23, 100)}')
    file.close()
    return path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:15'
    )

import pytest
import os
from src.class_connector import Connector

@pytest.fixture
def test_data():
    return [
        {
            "vacancy_id": "98384700",
            "vacancy_name": "Стажер Программист-разработчик Python",
            "vacancy_url": "https://api.hh.ru/vacancies/98384700?host=hh.ru",
            "api": "HeadHunter",
            "salary_from": 0,
            "salary_to": 50000,
            "currency": "RUR",
            "employer": "VITA STIMUL GRAND",
            "schedule": "Полный день"
        },
        {
            "vacancy_id": "98919945",
            "vacancy_name": "Junior Python-разработчик",
            "vacancy_url": "https://api.hh.ru/vacancies/98919945?host=hh.ru",
            "api": "HeadHunter",
            "salary_from": 40000,
            "salary_to": 60000,
            "currency": "RUR",
            "employer": "EasyDev",
            "schedule": "Гибкий график"
        },
        {
            "vacancy_id": "99180437",
            "vacancy_name": "Стажер-Разработчик",
            "vacancy_url": "https://api.hh.ru/vacancies/99180437?host=hh.ru",
            "api": "HeadHunter",
            "salary_from": 10000,
            "salary_to": 30000,
            "currency": "RUR",
            "employer": "Держава , АКБ",
            "schedule": "Гибкий график"
        },
    ]

@pytest.fixture
def test_query():
    return "test_vacancy_name"

@pytest.fixture
def test_instance(test_query, test_data):
    return Connector(test_query, test_data)

def test_insert(test_instance, test_query):
    test_instance.insert()
    file_path = f"data/{test_query}.json"
    assert os.path.exists(file_path)

def test_select(test_instance, test_query, test_data):
    test_instance.insert()
    selected_vacancies = test_instance.select()
    assert len(selected_vacancies) == len(test_data)
    for i in range(len(test_data)):
        assert selected_vacancies[i].vacancy_name == test_data[i]["vacancy_name"]
        assert selected_vacancies[i].salary_from == test_data[i]["salary_from"]

def test_sorted_salary(test_instance, test_data):
    sorted_vacancies = test_instance.sorted_salary()
    assert len(sorted_vacancies) == len(test_data)
    sorted_salaries = [vacancy.salary_from for vacancy in sorted_vacancies]
    assert sorted(sorted_salaries, reverse=True) == sorted_salaries

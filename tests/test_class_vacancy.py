import pytest
from src.class_vacancy import Vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(vacancy_id=1, vacancy_name="Junior Python-разработчик", vacancy_url="https://api.hh.ru/vacancies/98903376?host=hh.ru", api="HhApi",
                   salary_from=50000, salary_to=70000, currency="RUR", employer="Example Company", schedule="Гибкий график")


def test_vacancy_attributes(sample_vacancy):
    assert sample_vacancy.vacancy_id == 1
    assert sample_vacancy.vacancy_name == "Junior Python-разработчик"
    assert sample_vacancy.vacancy_url == "https://api.hh.ru/vacancies/98903376?host=hh.ru"
    assert sample_vacancy.api == "HhApi"
    assert sample_vacancy.salary_from == 50000
    assert sample_vacancy.salary_to == 70000
    assert sample_vacancy.currency == "RUR"
    assert sample_vacancy.employer == "Example Company"
    assert sample_vacancy.schedule == "Гибкий график"


def test_vacancy_str_representation(sample_vacancy):
    expected_output = f"""
                Id: 1\n
                Вакансия: Junior Python-разработчик\n
                Ссылка: https://api.hh.ru/vacancies/98903376?host=hh.ru\n
                Зарплата: от 50000 - до 70000 (RUR)\n
                Работодатель: Example Company\n
                График: Гибкий график               
                """
    assert str(sample_vacancy) == expected_output


def test_vacancy_comparison(sample_vacancy):
    other_vacancy = Vacancy(vacancy_id=2, vacancy_name="Стажер-разработчик", vacancy_url="https://api.hh.ru/vacancies/89753481?host=hh.ru", api="HhApi",
                            salary_from=0, salary_to=50000, currency="RUR", employer="Example Company",
                            schedule="Удаленная работа")

    assert sample_vacancy > other_vacancy
    assert not sample_vacancy <= other_vacancy

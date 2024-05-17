import pytest
from src.class_api import HhApi


class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data


@pytest.fixture
def mock_response():
    return MockResponse(status_code=200, json_data={"items": [
        {"id": 1, "name": "Junior Python-разработчик", "url": "https://api.hh.ru/vacancies/98919945?host=hh.ru",
         "salary": {"from": 50000, "to": 70000, "currency": "RUR"}, "employer": {"name": "Example Company"},
         "schedule": {"name": "Удаленная работа"}}]})


@pytest.fixture
def hh_api_instance():
    return HhApi(query="Junior Python-разработчик")


def test_get_request_success(hh_api_instance, mock_response, monkeypatch):
    def mock_get_request():
        return mock_response
    monkeypatch.setattr(hh_api_instance, 'get_request', mock_get_request)
    response = hh_api_instance.get_request()
    expected_response = {"items": [
        {"id": 1, "name": "Junior Python-разработчик", "url": "https://api.hh.ru/vacancies/98919945?host=hh.ru",
         "salary": {"from": 50000, "to": 70000, "currency": "RUR"}, "employer": {"name": "Example Company"},
         "schedule": {"name": "Удаленная работа"}}]}
    assert response.json_data == expected_response


def test_get_vacancies(hh_api_instance, mock_response, monkeypatch):
    hh_api_instance.get_request = lambda: mock_response.json_data
    vacancies = hh_api_instance.get_vacancies(page_count=1)
    assert len(vacancies) == 1
    assert vacancies[0]["id"] == 1
    assert vacancies[0]["name"] == "Junior Python-разработчик"
    assert vacancies[0]["url"] == "https://api.hh.ru/vacancies/98919945?host=hh.ru"
    assert vacancies[0]["salary"]["from"] == 50000
    assert vacancies[0]["salary"]["to"] == 70000
    assert vacancies[0]["salary"]["currency"] == "RUR"
    assert vacancies[0]["employer"]["name"] == "Example Company"
    assert vacancies[0]["schedule"]["name"] == "Удаленная работа"


def test_get_output_vacancies(hh_api_instance):
    hh_api_instance.vacancies = [
        {"id": 1, "name": "Junior Python-разработчик", "url": "https://api.hh.ru/vacancies/98919945?host=hh.ru",
         "salary": {"from": 50000, "to": 70000, "currency": "RUR"}, "employer": {"name": "Example Company"},
         "schedule": {"name": "Удаленная работа"}}]
    output_vacancies = hh_api_instance.get_output_vacancies()
    assert len(output_vacancies) == 1
    assert output_vacancies[0]["vacancy_id"] == 1
    assert output_vacancies[0]["vacancy_name"] == "Junior Python-разработчик"
    assert output_vacancies[0]["vacancy_url"] == "https://api.hh.ru/vacancies/98919945?host=hh.ru"
    assert output_vacancies[0]["api"] == "HeadHunter"
    assert output_vacancies[0]["salary_from"] == 50000
    assert output_vacancies[0]["salary_to"] == 70000
    assert output_vacancies[0]["currency"] == "RUR"
    assert output_vacancies[0]["employer"] == "Example Company"
    assert output_vacancies[0]["schedule"] == "Удаленная работа"

from abc import ABC, abstractmethod
from src.exceptions import ParsingError
import requests
import json
import os


class Parser(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HhApi(Parser):
    """Класс api headhunter"""

    url = "https://api.hh.ru/vacancies/"

    def __init__(self, query):
        self.params = {
            "per_page": 100,
            "page": int,
            "text": query,
            "archived": False,
        }
        self.vacancies = []

    def get_request(self):
        response = requests.get(self.url, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка выполнения запроса: {response.status_code}')
        return response.json()

    def get_vacancies(self, page_count=1):
        self.vacancies = []
        for page in range(page_count):
            vacancies_list = []
            self.params["page"] = page
            print(f'{self.__class__.__name__} - страница вакансий _{page}_:', end="")
            try:
                vacancies_list = self.get_request()
            except ParsingError as e:
                print(e)
            else:
                self.vacancies.extend(vacancies_list["items"])
                print(f'Получено вакансий - {len(vacancies_list)}')
                if len(vacancies_list) == 0:
                    print('Вакансий нет')
                    break
        return self.vacancies

    def get_output_vacancies(self):
        output_vacancies = []
        for vacancy in self.vacancies:
            output_vacancy = {
                "vacancy_id": vacancy["id"],
                "vacancy_name": vacancy["name"],
                "vacancy_url": vacancy["url"],
                "api": "HeadHunter",
                "salary_from": vacancy["salary"]["from"] if vacancy["salary"]["from"] else None,
                "salary_to": vacancy["salary"]["to"] if vacancy["salary"]["to"] else None,
                "currency": vacancy["salary"]["currency"] if vacancy["salary"]["currency"] else None,
                "employer": vacancy["employer"]["name"] if vacancy["employer"]["name"] else None,
                "schedule": vacancy["schedule"]["name"] if vacancy["schedule"]["name"] else None,
            }
            output_vacancies.append(output_vacancy)
        return output_vacancies

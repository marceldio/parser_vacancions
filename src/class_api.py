from abc import ABC, abstractmethod
from src.exceptions import ParsingError
import requests
import json
import os

class Parser(ABC):
    "Абстрактый класс"

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class HhApi(Parser):
    "Класс api headhunter"

    url = "https://api.hh.ru/vacancies/"

    def __init__(self, query):
        self.params = {
            "per_page": 100,
            "page": int,
            "text": query,
            "archived": False,
        }
        self.vacancies = []



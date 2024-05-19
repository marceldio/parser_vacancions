from src.class_vacancy import Vacancy
import json
import os


class Connector:

    def __init__(self, query, vacancies_json):
        """Функция конструктора создания файла по запросу"""
        self.filename = f"{query}.json"
        self.data_folder = "data"  # Имя папки для хранения файлов с вакансиями
        self.file_path = os.path.join(self.data_folder, self.filename)
        self.vacancies_json = vacancies_json


    def insert(self):
        """Записываем файл в папку data"""
        # Проверяем, существует ли папка data
        if not os.path.exists(self.data_folder):
            # Если папки нет, создаем ее
            os.makedirs(self.data_folder)

        # Записываем файл в папку data
        with open(self.file_path, "w", encoding="UTF-8") as file:
            json.dump(self.vacancies_json, file, indent=4, ensure_ascii=False)

    def select(self):
        """Читаем полученный файл"""
        # Проверяем, существует ли файл
        if not os.path.exists(self.file_path):
            # Если файла нет, возвращаем пустой список
            return []

        # Читаем файл из папки data
        with open(self.file_path, "r", encoding="UTF-8") as file:
            vacancies = json.load(file)
        return [Vacancy(**i) for i in vacancies]

    def sorted_salary(self):
        """Сортируем вакансии по зарплате"""
        # Читаем данные из файла, создаем список вакансий
        with open(self.file_path, "r", encoding="UTF-8") as file:
            vacancies = json.load(file)
            self.vacancies = [Vacancy(**i) for i in vacancies]
            # Сортируем список вакансий по зарплате
            self.vacancies.sort(reverse=True)
            return self.vacancies

class Vacancy:
    def __init__(self, vacancy_id, vacancy_name, vacancy_url, api, salary_from, salary_to, currency, employer, schedule):
        self.vacancy_id = vacancy_id
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.api = api
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.schedule = schedule

    def __str__(self):
        return f"""
                Id: {self.vacancy_id}\n
                Вакансия: {self.vacancy_name}\n
                Ссылка: {self.vacancy_url}\n
                Зарплата: от {self.salary_from} - до {self.salary_to} ({self.currency})\n
                Работодатель: {self.employer}\n
                Удаленно: {self.schedule}               
                """

    def __ge__(self, other):
        if self.salary_from and other.salary_from != None:
            return self.salary_from >= other.salary_from

    def __lt__(self, other):
        if self.salary_from and other.salary_from != None:
            return self.salary_from < other.salary_from





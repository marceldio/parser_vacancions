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
                График: {self.schedule}               
                """

    def __gt__(self, other):
        if self.salary_from is not None and other.salary_from is not None:
            return self.salary_from > other.salary_from
        elif self.salary_from is not None and other.salary_to is None:
            return True
        else:
            return False

    def __le__(self, other):
        """
        Вызывается при использовании оператора '<='. Вызывает __gt__ для обратного сравнения.
        """
        return other.__gt__(self)

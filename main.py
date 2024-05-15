from src.class_connector import Connector
from src.class_api import HhApi


def main():
    vacancies_json = []
    query = input('Введите запрос для поиска:__ ').title().strip()
    page_count = int(input('Введите количество страниц(100 вакансий на странице):__ '))

    """Создание экземпляра класса"""
    hh_answer = HhApi(query)

    """Получение вакансий"""
    hh_answer.get_vacancies(page_count=page_count)
    vacancies_json.extend(hh_answer.get_output_vacancies())

    connector = Connector(query=query, vacancies_json=vacancies_json)
    connector.insert()
    connector.select()
    connector.sorted_salary()

    while True:
        command = input("1 - Показать список\n"
                        "2 - Сортировать по з/п\n"
                        "0 - Выход\n"
                        "Ожидаю ввод команды:__ ")

        if command == "0":
            break
        elif command == "1":
            vacancies = connector.select()
        elif command == "2":
            vacancies = connector.sorted_salary()
        else:
            print("Ошибка ввода, введите одну из трех команд:")
            continue
        for vacancy in vacancies:
            print(vacancy, end="\n")


if __name__ == "__main__":
    main()

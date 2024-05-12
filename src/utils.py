import requests
from bs4 import BeautifulSoup

ITEMS = 100  # кол-во выводимых вакансий на одной странице (можно: 20, 50, 100)
# URL = 'https://hh.ru/search/vacancy?L_save_area=true&text=Python&search_field=name&search_field=description&excluded_text=&professional_role=96&area=1&salary=&currency_code=RUR&education=not_required_or_not_specified&experience=doesNotMatter&order_by=relevance&search_period=0&hhtmFrom=vacancy_search_filter&items_on_page={ITEMS}'
URL = f'https://hh.ru/search/vacancy?L_save_area=true&text=Python&search_field=name&search_field=description&excluded_text=&professional_role=96&area=1&salary=&currency_code=RUR&education=not_required_or_not_specified&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page={ITEMS}&hhtmFrom=vacancy_search_filter'
headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def extract_max_page():
    response = requests.get(URL, headers=headers)
    hh_soup = BeautifulSoup(response.text, 'html.parser')
    paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})
    pages = []
    for page in paginator:
        pages.append(int(page.find('a').text))
    return pages[-1]


def extract_hh_offers(last_page):
    hh_offers = []
    # for page in range(last_page):
    #     result = requests.get(f'{URL}&page={page}', headers=headers)
    result = requests.get(f'{URL}&page=0', headers=headers)
    # print(result.status_code)
    extract_soup = BeautifulSoup(result.text, 'html.parser')
    results = extract_soup.find_all('div', {'class': 'vacancy-serp-item__layout'})
    for result in results:
        title = result.find('a').text
        company = result.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
        print(f'{title}, {company}')
        # print(company)
    # return hh_offers


extract_hh_offers(0)

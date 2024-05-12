from src.utils import extract_max_page, extract_hh_offers

max_page = extract_max_page()
print(max_page)

hh_offers = extract_hh_offers(max_page)
print(hh_offers)

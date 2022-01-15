#!/usr/bin/python3

import requests

response = requests.get(
    'https://www.banki.ru/investment/search/share/ajax/?is_foreign=0&term=1year&sort_field=price_diff_percent&sort_order=desc&page=2&is_popular=true',
    headers={
        "x-requested-with": "XMLHttpRequest"})
print(response.status_code)

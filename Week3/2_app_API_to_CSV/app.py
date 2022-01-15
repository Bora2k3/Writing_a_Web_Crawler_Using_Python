import requests
import os

terms = ['1day', '1month', '1year', '2year']

def getInfo(is_foreign, term, page):
    link = f'https://www.banki.ru/investment/search/share/ajax/?is_foreign={is_foreign}&{term}&page={page}&is_popular=true'
    response = requests.get(link,
                            headers = {"x-requested-with": "XMLHttpRequest"})
    return [row for row in response.json()['data']['shares']]

def write2csv(lst, is_foreign, term):
    fileName = f'result/is_foreign_{is_foreign}__term_{term}.csv'
    flag = 'a' if os.path.exists(fileName) else 'w'

    with open(fileName, flag) as f:
        for row in lst:
            csv_row = f"{row['name']},{row['price_current_rur']},{row['price_diff_percent']}"
            f.write(csv_row+'\n')

def crawl():
    for is_foreign in range(2):
        for term in terms:
            i = 1
            while True:
                result = getInfo(is_foreign, term, i)
                if len(result) == 0:
                    break
                print(f'page: {i} term: {term} is_foreign: {is_foreign}')
                write2csv(result, is_foreign, term)
                i += 1

try:
    crawl()
except KeyboardInterrupt:
    print('[-] process stopped')
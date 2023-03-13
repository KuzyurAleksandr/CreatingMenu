from bs4 import BeautifulSoup;
import requests
import json

def get_list_of_groops():
    url = 'https://health-diet.ru/table_calorie/'
    header = {'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 96.0) Gecko / 20100101  Firefox / 96.0'}
    result = requests.get(url, header)
    result.encoding = 'UTF-8'
    src = result.text
    with open('calorie_foods\list_of_groops.html', 'w', encoding='utf-8') as file:
        file.write(src)

def get_calorie_foods():
    get_list_of_groops()

def main():
    # База калорийности продуктов
    get_calorie_foods()

if __name__=='__main__':
    main()
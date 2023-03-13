from bs4 import BeautifulSoup;
import requests
import json


def get_list_of_groops():
    url = 'https://health-diet.ru/table_calorie/'
    header = {'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 96.0) Gecko / 20100101  Firefox / 96.0'}
    result = requests.get(url, header)
    result.encoding = 'UTF-8'
    src = result.text
    with open('..\calorie_foods\list_of_groops.html', 'w', encoding='utf-8') as file:
        file.write(src)

def prepare_groops():
    with open('..\calorie_foods\list_of_groops.html','r',encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_hrefs_of_groops = soup.findAll(class_="mzr-tc-group-item-href")

    dict_of_groops = {}
    for groop in all_hrefs_of_groops:
        dict_of_groops[groop.text] = 'https://health-diet.ru'+groop.get('href')

    with open('..\calorie_foods\dict_all_groops.json','w',encoding='utf-8') as file_json:
        json.dump(dict_of_groops,file_json,indent=4,ensure_ascii=False)

def handle_groops():
    with open('..\calorie_foods\dict_all_groops.json','r',encoding='utf-8') as file_json:
        dict_groops = json.load(file_json)

    not_needed_symbols = ["'"," ","-",","]
    for groop_name, groop_href in dict_groops.items():
        for symbol in not_needed_symbols:
            if symbol in groop_name:
                groop_name = groop_name.replace(symbol,"_")

        print(groop_name)

def get_calorie_foods():
    #get_list_of_groops()
    #prepare_groops()
    handle_groops()


def main():
    # База калорийности продуктов
    get_calorie_foods()


if __name__ == '__main__':
    main()

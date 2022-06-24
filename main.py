import requests
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)


# with open('index.html', 'w') as file:
#   file.write(src)


# with open('index.html') as file:
#   src = file.read()

# soup = BeautifulSoup(src, 'lxml')

# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')


# all_categories_dict = {}

# for item in all_products_hrefs:
#   item_text = item.text
#   item_href = 'https://health-diet.ru' + item.get('href')

#   all_categories_dict[item_text] = item_href

# with open('all_categories_dict.json', 'w') as file:
#   json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


with open('all_categories_dict.json') as file:
  all_categories = json.load(file)


count = 0
for category_name, category_href in all_categories.items():

  if count == 0:
    rep = [',', ' ', '-', '\'']
    for item in rep:
      if item in category_name:
        category_name = category_name.replace(item, '_')
    
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{category_name}.html', 'w') as file:
      file.write(src)

    with open(f'data/{count}_{category_name}.html') as file:
      src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    #собираем заголовки таблиц
    table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f'data/{count}_{category_name}.csv', 'w', encoding='utf-8') as file:
      writer = csv.writer(file)
      writer.writerow(
        (
          product,
          calories,
          proteins,
          fats,
          carbohydrates,
        )
      )

      #собираем данные продуктов
      products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

      for item in products_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        with open(f'data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow(
            (
              title,
              calories,
              proteins,
              fats,
              carbohydrates,
            )
          )

    

    count += 1



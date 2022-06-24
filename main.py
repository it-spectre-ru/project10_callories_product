import requests
from bs4 import BeautifulSoup
import json

# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

# headers = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }

# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)


# with open('index.html', 'w') as file:
#   file.write(src)


with open('index.html') as file:
  src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')


all_categories_dict = {}

for item in all_products_hrefs:
  item_text = item.text
  item_href = 'https://health-diet.ru/' + item.get('href')

  all_categories_dict[item_text] = item_href

with open('all_categories_dict.json', 'w') as file:
  json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


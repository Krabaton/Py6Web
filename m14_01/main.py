import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re

base_url = 'https://index.minfin.com.ua/ua/russian-invading/casualties'

urls = ['/', '/month.php?month=2022-08', '/month.php?month=2022-07', '/month.php?month=2022-06',
        '/month.php?month=2022-05', '/month.php?month=2022-04', '/month.php?month=2022-03', '/month.php?month=2022-02']

data = []

for url in urls:
    response = requests.get(base_url + url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('ul[class=see-also] li[class=gold]')

    for element in content:
        result = {}
        date = element.find('span', attrs={"class": "black"}).text
        try:
            date = datetime.strptime(date, "%d.%m.%Y").isoformat()
        except ValueError:
            print(f'Error for {date}')
            continue

        result.update({"date": date})
        losses = element.find('div', attrs={"class": "casualties"}).find('div').find('ul')
        for l in losses:
            title, quantity = l.text.split("—")
            title = title.strip()
            quantity = re.search(r"\d+", quantity).group()
            result.update({title: int(quantity)})
        data.append(result)


with open('data.json', "w", encoding='utf-8') as fd:
    json.dump(data, fd, ensure_ascii=False)

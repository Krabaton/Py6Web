import json
import re
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from dateutil import parser
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import TypeLosses, Losses
from .mongodb.connect import db

# Create your views here.

def main(request):
    results = Losses.objects.raw("""
        SELECT itl.id, itl.name, itl.description, il.total, il.updated_at
        FROM infoboard_losses as il
        JOIN infoboard_typelosses as itl ON itl.id = il.lose_name_id
    """)
    print(results)
    return render(request, 'infoboard/index.html', {"results": results})


def get_losses_actual(request):
    now_date = datetime.strftime(datetime.now(), "%d.%m.%Y")
    result = scraping([now_date])
    print(result[0])
    if len(result) > 0:
        result[0].pop('date')
        for key, value in result[0].items():
            name = TypeLosses.objects.get(name=key)
            # l = Losses.objects.filter(lose_name=name).first()
            # if l is None:
            #     r = Losses(lose_name=name, total=value)
            #     r.save()
            # else:
            Losses.objects.filter(lose_name=name).update(total=value)

    return redirect('main')


def losses_list(request):
    results = db.losses.find(sort=[("date", -1)])
    return render(request, 'infoboard/losses-list.html', {"results": transform_data_for_losses_list(results)})


def get_chart(request, id):
    name = str(TypeLosses.objects.get(pk=id))
    return render(request, 'infoboard/chart.html', {"namelose": name})


def get_chart_info(request, id, day=24, month=2):
    name = str(TypeLosses.objects.get(pk=id))
    date_start = datetime(year=2022, day=day, month=month).isoformat()
    date_finish = datetime.now().isoformat()
    records = db.losses.find({"$and": [{"date": {"$gte": date_start}}, {"date": {"$lte": date_finish}}]},
                             {'date': 1, name: 1, '_id': 0}, sort=[('date', 1)])
    result = json.dumps(list(records))
    return HttpResponse(result, content_type='application/json')


def sync_losses_list(request):
    last_result = db.losses.find_one(sort=[("date", -1)])
    if last_result is not None:
        date = last_result["date"]
        last_date = parser.parse(date)
        now_date = datetime.now()
        period = now_date - last_date
        search_list = []
        for day in range(1, period.days + 1):
            next_date = last_date + timedelta(days=day)
            search_list.append(datetime.strftime(next_date, "%d.%m.%Y"))
        data_to_insert = scraping(search_list)
        print(data_to_insert)
        if len(data_to_insert) > 0:
            db.losses.insert_many(data_to_insert)
    return redirect("losseslist")


def transform_data_for_losses_list(data):
    result = []
    for el in data:
        date = datetime.strftime(parser.parse(el['date']), '%d.%m.%Y')
        list_tuple = []
        for key, value in el.items():
            if key != '_id' and key != 'date':
                list_tuple.append((key, value))
        result.append((date, list_tuple))
    return result


def scraping(date_list: list) -> list:
    url = 'https://index.minfin.com.ua/ua/russian-invading/casualties/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select_one('ul[class=see-also] > li[class=gold]')

    result = []

    for current_date in date_list:
        result_date = {}
        result_date.update({"date": datetime.strptime(current_date, "%d.%m.%Y").isoformat()})
        try:
            losses = content.find('span', attrs={"class": "black"}, text=current_date).parent \
                .find('div', attrs={"class": "casualties"}).find('div').find('ul')
        except AttributeError as err:
            print(f'Error for {err}')
            continue

        for l in losses:
            title, quantity = l.text.split("—")
            title = title.strip()
            quantity = re.search(r"\d+", quantity).group()
            result_date.update({title: int(quantity)})
        result.append(result_date)
    return result

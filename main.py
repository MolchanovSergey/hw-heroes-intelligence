import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
# создадим список, интересующих супергероев, укажем атрибут и имя как бы они выгляделти в файле json,
heroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
# для каждого героя получим данные с помощью запроса
for hero in heroes:
    hero_response = requests.get(url + hero['name'])
    # print(hero_response.text)
    # находим значение параметра intelligence для каждого героя
    hero['intelligence'] = int(hero_response.json()['results'][0]['powerstats']['intelligence'])
# сортируем имяна героев по занчению intelligens c конца и выводим первое
print(sorted(heroes, key=lambda hero: -hero['intelligence'])[0]['name'])


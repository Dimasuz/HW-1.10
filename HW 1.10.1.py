import requests

heroes = ['Hulk', 'Captain America', 'Thanos']

url = 'https://superheroapi.com/api/2619421814940190/search/'

intelligest = {'name': '', 'intelligence': 0}

for i in heroes:
    resp = requests.get(url + i)
    intelligence = int(resp.json()['results'][0]['powerstats']['intelligence'])
    # print(i)
    # print(intelligence)

    if intelligest['intelligence'] < intelligence:
        intelligest['intelligence'] = intelligence
        intelligest['name'] = i
    elif intelligest['intelligence'] == intelligence:
        intelligest['name'] = intelligest['name'] + ', ' + i

print('Самый умный:', intelligest['name'])

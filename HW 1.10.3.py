
from pprint import pprint
import requests


class TagPython:
  def __init__(self, tagged: str):
     self.tagged = tagged

  def load(self):
  '''метод выводит все вопросы с задаваемым тегом за период с 29 по 30 мая 2022 года'''
    url = "https://api.stackexchange.com/2.3/questions"
    params = {'fromdate': '1653782400', 'todate': '1653955200', 'order': 'desc', 'sort': 'activity', 'tagged': tagged, 'site': 'stackoverflow'}
    responce = requests.get(url, params=params)
    responce.raise_for_status  
    pprint(responce.json())

if __name__ == '__main__':

  tagged = input('Введите искомый контекст: ')
  loader = TagPython(tagged)
  result = loader.load()
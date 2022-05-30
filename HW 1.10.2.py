
from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file, path_on_yd):
        """Метод загружает файл на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': path_on_yd, 'overwrite': 'true'}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        responce_url = requests.get(url, headers=headers, params=params)
        responce = requests.put(responce_url.json()['href'], data=open(path_to_file, 'rb'))
        responce.raise_for_status

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = 'AQ'
    uploader = YaUploader(token)
    path_to_file = input('Введите путь к исходному файлу: ')
    path_on_yd = input('Введите путь к конечному файлу: ')
    result = uploader.upload(path_to_file, path_on_yd)


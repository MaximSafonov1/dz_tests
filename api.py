import requests
import json


file_url = 'https://cloud-api.yandex.net/v1/disk/resources'
token = ''
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
            }


def create_folder(folder_name):
    params = {
        'path': folder_name
    }
    response = requests.put(file_url, headers=headers, params=params)
    # print(response)
    return response


def folder_existence(folder_name):
    create_folder('file')
    params = {
        'path': folder_name
    }
    result = requests.get(file_url, headers=headers, params=params)
    # print(result)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')


folder_existence('file')

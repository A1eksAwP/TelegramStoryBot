"""
This is my simple parser for automatic made KATA.py files to solution a new kata from codewars URL.
"""
import requests
import json
import re


class Kata:
    def __init__(self, url):
        self.kata_url = url
        self.kata_id = None
        self.response_url = None
        self.response = None
        self.response_json = None
        self.kata_dict = None
        self.new_file = None

    def start_parser(self):
        if not re.fullmatch(r'(https://)?(www\.codewars\.com)?(/)?kata/[^/]+(/train/python)?', self.kata_url):
            return 'Ваш URL не относится к codewars.'
        self.kata_id = re.search(r'/kata/?(?P<id>[^/]+)', self.kata_url).group('id')
        self.response_url = f'https://www.codewars.com/api/v1/code-challenges/{self.kata_id}'
        self.response = requests.get(self.response_url, timeout=1000)
        self.set_kata_dict()
        return self.get_kata_dict()

    def set_kata_dict(self):
        if self.response.status_code == 200:
            self.response_json = json.loads(self.response.content)
            self.kata_dict = {
                'id': self.response_json['id'],
                'title': self.response_json['slug'],
                'kyu': self.response_json['rank']['name'],
                'description': self.response_json['description'],
                'tags': self.response_json['tags']
            }
        else:
            self.kata_dict = 'Ошибка извлечения данных'

    def get_kata_dict(self):
        return self.kata_dict

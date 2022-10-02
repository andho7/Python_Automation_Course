import json
import random
import re

import requests
from bs4 import BeautifulSoup


class WebAPI:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.user_data = None
        self.base_url = 'https://www.aqa.science/'
        self.url = f'{self.base_url}api-auth/login/?next=/'
        self.session = requests.Session()
        self.session.get(self.url)
        html = self.session.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        input_tag = soup.find(attrs={"name": "csrfmiddlewaretoken"})
        self.token_csrf = input_tag['value']

    def login(self):
        payload = {'username': 'admin', 'password': 'admin123', 'csrfmiddlewaretoken': self.token_csrf}
        r = self.session.post(url=self.url,
                              data=payload,
                              headers={'Referer': 'https://www.aqa.science/api-auth/login/?next=/'}
                              )
        print('=========Logged in========')
        return r.status_code

    def logout(self):
        r = self.session.get(f'{self.base_url}logout/')
        print('=========Logged out========')
        return r.status_code

    def generate_username(self):
        username = f'user_name_test_{random.randint(1, 100)}'
        while self.is_username(username):
            username = f'user_name_test_{random.randint(1, 100)}'

        return username

    def create_user(self, username):
        user_data = {
            "username": username,
            "email": "",
            "groups": []
        }
        r2 = self.session.get(url=f'{self.base_url}users/',
                              headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                                                 'image/avif,image/webp,image/apng,*/*;q=0.8,'
                                                 'application/signed-exchange;v=b3;q=0.9'}).text
        csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
        r = self.session.post(f'{self.base_url}users/',
                              json=user_data,
                              headers={'Content-Type': 'application/json', 'X-CSRFTOKEN': csrf,
                                       'Referer': 'https://www.aqa.science/users'})

        self.username = r.json()['username']
        self.user_id = re.findall(r'\d+', r.json()['url'])[0]
        self.user_data = r.json()

        return r.status_code

    def get_user_data(self):
        r2 = self.session.get(url=f'{self.base_url}users/{self.user_id}',
                              headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                                                 'image/avif,image/webp,image/apng,*/*;q=0.8,'
                                                 'application/signed-exchange;v=b3;q=0.9'}).text
        csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
        r = self.session.get(f'{self.base_url}users/{self.user_id}',
                             headers={'Content-Type': 'application/json', 'X-CSRFTOKEN': csrf,
                                      'Referer': f'https://www.aqa.science/users/{self.user_id}'})
        user_data = r.json()
        return user_data

    def is_user_data_equal(self):
        user_data = self.get_user_data()
        return user_data == self.user_data

    def update_username(self):
        username = 'user_name_test_updated'
        user_data = {
            "username": username
        }
        r2 = self.session.get(url=f'{self.base_url}users/{self.user_id}',
                              headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                                                 'image/avif,image/webp,image/apng,*/*;q=0.8,'
                                                 'application/signed-exchange;v=b3;q=0.9'}).text
        csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
        r = self.session.put(f'{self.base_url}users/{self.user_id}/', json=user_data,
                             headers={'Content-Type': 'application/json', 'X-CSRFTOKEN': csrf,
                                      'Referer': f'https://www.aqa.science/users/{self.user_id}'})

        self.username = username

        return r.status_code

    def delete_user(self):
        r2 = self.session.get(url=f'{self.base_url}users/{self.user_id}',
                              headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                                                 'image/avif,image/webp,image/apng,*/*;q=0.8,'
                                                 'application/signed-exchange;v=b3;q=0.9'}).text
        csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
        r = self.session.delete(f'{self.base_url}users/{self.user_id}',
                                headers={'Content-Type': 'application/json', 'X-CSRFTOKEN': csrf,
                                         'Referer': f'https://www.aqa.science/users/{self.user_id}'})

        return r.status_code

    def get_all_users(self):
        r2 = self.session.get(f'{self.base_url}users/')
        result = []
        r2 = r2.json()
        temp_result = r2["results"]
        result.extend(temp_result)

        while True:
            next_url = r2["next"]
            if not next_url:
                break
            r2 = requests.get(next_url, auth=("admin", "admin123")).json()
            result.extend(r2['results'])

        with open('response.json', 'w') as r:
            json.dump(result, r)

        return result

    def is_username(self, username):
        users_list = self.get_all_users()
        for user in users_list:
            if user['username'] == username:
                self.user_id = re.findall(r'\d+', user['url'])[0]
                return True, self.user_id
            return False

# import json
# import re
#
# import requests
# from bs4 import BeautifulSoup


# result = []
#
# # url = 'https://www.aqa.science/'
#
# response = requests.get(url).json()
# received_url = response['users']
# response_new = requests.get(received_url, auth=("admin", "admin123")).json()
# temp_result = response_new["results"]
# result.extend(temp_result)
#
# while True:
#     next_url = response_new["next"]
#     if not next_url:
#         break
#     response_new = requests.get(next_url, auth=("admin", "admin123")).json()
#     result.extend(response_new['results'])
#
# with open('response.json', 'w') as r:
#     json.dump(result, r)

# url = 'https://www.aqa.science/users/1097/'
# r = requests.get(url, auth=("admin", "admin123")).json()
# print(r)

# html = #the HTML code you've written above
# parsed_html = BeautifulSoup(html)
# print(parsed_html.body.find('div', attrs={'class':'container'}).text)

# url = 'https://www.aqa.science/api-auth/login/?next=/'
# s = requests.Session()
# response = s.get(url=url)
# print(s.headers.items())
# print(s.cookies.items())
# s = requests.session()
# print(s.cookies.values())
# response = s.get(url=url)
# print(response.cookies.items())
# print(response.text)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# input_tag = soup.find(attrs={"name": "csrfmiddlewaretoken"})
# output = input_tag['value']
# csrf = response.cookies.values()
# print(output)
# print(csrf[0])
#
# header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                         'Chrome/105.0.0.0 Safari/537.36', 'Referer': 'https://www.aqa.science/api-auth/login/?next=/',
#           'Cookie': 'csrftoken=' + csrf[0]}
# cookies = {'Cookie': 'csrftoken=' + csrf[0] +'; sessionid=at282rijhy0bnvaxxyfp6jtc3ege86o6'}
# payload = {
#     'username': 'admin',
#     'password': 'admin123',
#     'csrfmiddlewaretoken': output
# }

# #
# s = requests.Session()
# login_req = s.post(url, headers=header, data=payload, cookies=cookies)
# print(login_req.text)
# print(login_req.cookies.values(), '=======')
# # print(cookies)
# r = requests.get('https://www.aqa.science/users/', headers=header, cookies=cookies, data=payload).json()
# print(r)


# url_login = 'https://www.aqa.science/api-auth/login/'
#
# client = requests.session()
# client.get(url_login)
# csrftoken = client.cookies['csrftoken']
# print(client.headers)
# print(csrftoken)
# # html = client.text
# # soup = BeautifulSoup(html, 'html.parser')
# # input_tag = soup.find(attrs={"name": "csrfmiddlewaretoken"})
# # token_csrf = input_tag['value']
# login_data = {'username': 'admin', 'password': 'admin123', 'csrfmiddlewaretoken': 'token_csrf', 'next': '/users/'}
# r1 = client.post(url_login, data=login_data)
# print(r1.text)
# # payload = {'csrfmiddlewaretoken': csrftoken, }
# # r2 = client.get('https://www.aqa.science/users/', payload)
# # print(r2.json)
#
# url = 'https://www.aqa.science/api-auth/login/?next=/'
# s = requests.Session()
# s.get(url)
# html = s.get(url).text
# soup = BeautifulSoup(html, 'html.parser')
# input_tag = soup.find(attrs={"name": "csrfmiddlewaretoken"})
# token_csrf = input_tag['value']
#
# payload = {'username': 'admin', 'password': 'admin123', 'csrfmiddlewaretoken': token_csrf}
# r = s.post(url=url,
#            data=payload,
#            headers={'Referer': 'https://www.aqa.science/api-auth/login/?next=/'}
#            )
# print(r.request.headers)
# r2 = s.get('https://www.aqa.science/users/1291')
# print(r2.json())
#
#
# data = {
#     "url": "https://www.aqa.science/users/1291/",
#     "username": "user111_2_1+1+6",
#     "email": "",
#     "groups": []
# }
# a = json.dumps(data, indent=4)
# r2 = s.get(url='https://www.aqa.science/users/1291/',
#            headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
#                               'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}).text
# csrf = re.search(r'(?<=csrfToken: ").*(?=")', r2)[0]
#
# r4 = s.put(url='https://www.aqa.science/users/1291/',
#            data=a,
#            headers={'Content-Type': 'application/json',
#                     'X-CSRFTOKEN': csrf,
#                     'Referer': 'https://www.aqa.science/users/1291/'})
# print(r4.request.headers)
# print(r4.request.body)
# print(r4.request.method)
# print(r4.status_code)
# print(r4.text)
12
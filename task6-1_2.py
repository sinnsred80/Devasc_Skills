import requests

# Diverse globale variabler
access_token = 'NmVkNWRjMzYtODAxZi00NDc4LWI3ZTktZTEwYzAwMmY2ZjVlNDZkYTUwNTEtNjJj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
url = 'https://webexapis.com/v1/rooms'

# Task 1 - Create a Webex Teams space
headers = {
        'Authorization': 'Bearer {}'.format(access_token),
'Content-Type': 'application/json'
}

params={'title': 'netacad devasc skills Patrick Mostad'}
res = requests.post(url, headers=headers, json=params)
print(res.json())

jsonResponse = res.json()

room_id = jsonResponse["id"]

person_email = 'atoxopeu@cisco.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())

# task 2 - send URL til github
message = 'This is the link to my reposotory: https://github.com/sinnsred80/Devasc_Skills'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Diverse globale variabler
access_token = 'NmVkNWRjMzYtODAxZi00NDc4LWI3ZTktZTEwYzAwMmY2ZjVlNDZkYTUwNTEtNjJj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNDM3NDQwMTAtYWQyNS0xMWVjLTlhZjYtMjE4MjE3NzdhNDI1'
message = 'Here are my screenshots of netacad-devasc skills-based exam'
url = 'https://webexapis.com/v1/messages'

# Task 3 - Send message
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())


# Task 4 - Send files
myfiles = ["task1.png", "task2.png", "task3.png", "task4.png", "task5.png", "task6.png", "task7.png"]
for i in myfiles:
    m = MultipartEncoder({
        'roomId': room_id,
        'text': 'Her er filen ' + i,
        'files': (i, open(i, 'rb'),'image/png')})

    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': m.content_type
    }

    res = requests.post(url, data=m, headers=headers, )
    print(res.text)


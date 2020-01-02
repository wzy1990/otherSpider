import requests
from json import loads

url = 'https://www.ximalaya.com/revision/play/album?albumId=4756811&pageNum=1&pageSize=30'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'xm-sign': '712ec03665585f6054d1332a9dcfd9a3(63)1559312670151(19)1559312686500'
}

response = requests.get(url, headers=header)
print(response.text)
album_data = loads(response.text)['data']['tracksAudioPlay']
print(album_data)

for album in album_data:
    name = album['src'].split('/')[-1]
    trackName = album['trackName'] + name
    with open('album/{}'.format(trackName), 'wb') as file:
        file.write(requests.get(album['src'], headers=header).content)
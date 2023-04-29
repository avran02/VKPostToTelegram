import requests
from config import API_KEY, PATH
import json
class Pars():

    def __init__(self):
        url = f'https://api.vk.com/method/wall.get?access_token={API_KEY}&v=5.131&owner_id=-34075676&count=2'
        self.page = requests.get(url).text
        self.js = json.loads(self.page)['response']['items']

    def pars_it(self):
        self.get_text()     
        self.get_photos()


    def get_text(self):
        for post in self.js:
            try:
                a = post['is_pinned']
                continue
            except:
                self.post = post
        with open(f'{PATH}/tmp/PostText.txt', 'w') as f:
            print(self.post['text'])
            f.write(self.post['text'])

    def get_photos(self):
        attachments = self.post['attachments']
        photos = list()
        for attachment in attachments:
            if attachment['type'] == 'photo':
                photos.append(attachment['photo']['sizes'][-1]['url'])
        for i in range(0, len(photos)):
            print(i)
            response = requests.get(photos[i])
            with open(f'{PATH}/tmp/photo{i}', "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    obj = Pars()
    obj.pars_it()
    print('Готово')

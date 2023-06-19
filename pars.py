import requests
from config import API_KEY, PATH
import json

class Pars():
    def __init__(self):
        url = f'https://api.vk.com/method/wall.get?access_token={API_KEY}&v=5.131&domain=job_isuct&count=3'# 2 HERE
        self.page = requests.get(url).text
        self.js = json.loads(self.page)['response']['items']
        # with open(f'{PATH}/tmp/resp', 'w') as f:
        #     json.dump(self.js, f, indent=4)

    def pars_it(self):
        self.__get_text(self.js, 'PostText')     
        self.__get_photos(self.post['attachments'], 'Photo')
        try:
            self.__get_text(self.post['copy_history'], 'FwPostText')
            self.__get_photos(self.post['attachments'], 'FwPhoto')
        except:
            print('exception')

    def pars_pinned_text(self):
        self.__get_pinned_text(self.js, 'PostText')     
        self.__get_photos(self.post['attachments'], 'Photo')
        try:
            self.__get_pinned_text(self.post['copy_history'], 'FwPostText')
            self.__get_photos(self.post['attachments'], 'FwPhoto')
        except:
            print('exception')

    def __get_pinned_text(self, item, name):
        self.post = item[0] 
        with open(f'{PATH}/tmp/{name}.txt', 'w') as f:
            f.write(self.post['text'])
        return self.post['text']

    def __get_text(self, item, name):
        for post in item:
            try:
                a = post['is_pinned']
                continue
            except:
                self.post = post
                break
        with open(f'{PATH}/tmp/{name}.txt', 'w') as f:
            f.write(self.post['text'])
        return self.post['text']

    def __get_photos(self, item, name):
        photos = list()
        for attachment in item:
            if attachment['type'] == 'photo':
                photos.append(attachment['photo']['sizes'][-1]['url'])
        for i in range(0, len(photos)):
            response = requests.get(photos[i])
            with open(f'{PATH}/tmp/{name}{i}', "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    exec = Pars()
    exec.pars_it()

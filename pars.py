import requests
from config import API_KEY, PATH
import json
# copy_history

class Pars():
    def __init__(self):
        url = f'https://api.vk.com/method/wall.get?access_token={API_KEY}&v=5.131&domain=job_isuct&count=3'# 2 HERE
        self.page = requests.get(url).text
        # print(f'\n\n\n{self.page}\n\n\n')
        self.js = json.loads(self.page)['response']['items']
        # with open(f'{PATH}/tmp/resp', "r") as f:
            # print(f.read(), '\n\n\n\n')
            # self.js  = json.load(f)
        # with open(f'{PATH}/tmp/resp', 'w') as f:
        #     json.dumps(self.js)

            


    def pars_it(self):
        self.__get_text(self.js, 'PostText')     
        self.__get_photos(self.post['attachments'], 'Photo')
        try:
            self.__get_text(self.post['copy_history'], 'FwPostText')
            self.__get_photos(self.post['attachments'], 'FwPhoto')
        except:
            print('exception')
        
        # print('done')
        # self.__get_links()
        # self.__get_fw_text()
        # self.__get_fw_photos()
        # self.__get_fw_links()

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

    def __get_photos(self, item, name):
        # attachments = self.post['attachments']
        photos = list()
        for attachment in item:
            if attachment['type'] == 'photo':
                photos.append(attachment['photo']['sizes'][-1]['url'])
        for i in range(0, len(photos)):
            print(i)
            response = requests.get(photos[i])
            with open(f'{PATH}/tmp/{name}{i}', "wb") as f:
                # f.write(f'{i} reg photo')
                f.write(response.content)

if __name__ == '__main__':
    exec = Pars()
    exec.pars_it()

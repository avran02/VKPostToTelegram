import telebot
from telebot.types import InputMediaPhoto
import os
from config import TOKEN, TG_CHAT_ID, PATH

#467380177
class Bot_poster():
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.image_files = None
        self.media_group = None
    
    def post_to_tg(self, text):
        self.find_photos()
        if self.image_files == []:
            print('21345wert')
            return False
        self.bot.send_media_group(chat_id=TG_CHAT_ID, media=self.media_group)      
        self.delete_tmp()
        self.bot.send_message(TG_CHAT_ID , text)
        return True

    def find_photos(self):
        files = os.listdir(f'{PATH}/tmp')
        self.image_files = [f for f in files if f.startswith('photo')]
        self.media_group = [InputMediaPhoto(open(f'{PATH}/tmp/' + f, 'rb')) for f in self.image_files]

    def delete_tmp(self):
        for i in self.image_files:
            os.remove(f'{PATH}/tmp/{i}')
        os.remove(f'{PATH}/tmp/PostText.txt')

if __name__ == '__main__':
    asd = Bot_poster()
    asd.post_to_tg('text')
    # print(asd.image_files)
    # print(asd.media_group)
    # asd.find_photos()
    # print(asd.image_files)    
    # print(asd.media_group)
    
    # asd.bot.send_message(467380177, 'ПОшёл нахуй Ваня')

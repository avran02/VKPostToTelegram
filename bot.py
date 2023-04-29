import telebot
from telebot.types import InputMediaPhoto
import os
from config import TOKEN, TG_CHAT_ID, PATH

class Bot_poster():
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
    

    def post_to_tg(self, text):
        self.bot.send_message(467380177 , text)
        self.bot.send_message(1542994061 , text)

        self.find_photos()
        self.bot.send_media_group(chat_id=467380177, media=self.media_group)
        self.find_photos()
        self.bot.send_media_group(chat_id=1542994061, media=self.media_group)
        self.delete_tmp()


    def find_photos(self):
        files = os.listdir(f'{PATH}/tmp')
        self.image_files = [f for f in files if f.startswith('photo')]
        self.media_group = [InputMediaPhoto(open(f'{PATH}/tmp/' + f, 'rb')) for f in self.image_files]


    def delete_tmp(self):
        for i in self.image_files:
            os.remove(f'{PATH}/tmp/{i}')
        os.remove(f'{PATH}/tmp/PostText.txt')
        print('deleted')

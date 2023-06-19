import telebot
from telebot.types import InputMediaPhoto
import os
from config import TOKEN, TG_CHAT_ID, PATH


class Bot_poster():
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
        self.files = None
        self.media_group = None

    def clear_folder(self):
        self.__find_photos()
        self.__clear_tmp()

    def post_to_tg(self, text):
        self.__find_photos()
        if self.files == []:
            return False
        self.bot.send_message(TG_CHAT_ID , text)
        self.bot.send_media_group(chat_id=TG_CHAT_ID, media=self.media_group)      
        self.__clear_tmp()
        return True

    def __find_photos(self):
        files = os.listdir(f'{PATH}/tmp')
        image_files = [f for f in files if f.startswith('Photo')]
        fw_image_files = [f for f in files if f.startswith('FwPhoto')]
        self.files = image_files + fw_image_files
        self.media_group = [InputMediaPhoto(open(f'{PATH}/tmp/' + f, 'rb')) for f in self.files]

    def __clear_tmp(self):
        for i in self.files:
            os.remove(f'{PATH}/tmp/{i}')
        with open (f'{PATH}/tmp/PostText.txt', "w") as f:
            f.write('')
        with open (f'{PATH}/tmp/FwPostText.txt', "w") as f:
            f.write('')
        self.media_group = []
        

if __name__ == '__main__':
    asd = Bot_poster()
    asd.post_to_tg('text')


from pars import Pars
from config import PATH
from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
import time
Builder.load_file('styles.kv')


class MyButton(Button):
    pass

Window.borderless = True
Window.size = (700, 500)
Window.clearcolor = (3/255, 53/255, 78/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.pars_btn = MyButton(
            text = 'Нажмите чтобы спарсить последнюю запись'
            # background_normal = ''
                                )
        self.label = TextInput(text = 'Здесь будет ваш текст')
        self.post_btn = MyButton(
            text = 'Нажмите чтобы запостить в телеграм'
            # background_normal = ''
                                )
                                

    def build(self):
        self.title = 'VK post to Telegram'
        self.box = BoxLayout(orientation = 'vertical', spacing = 5)
        self.pars_btn.bind(on_press = lambda x : self.pars_and_set_text())
        self.post_btn.bind(on_press = lambda x: Func.post(self, self.label.text))
        self.box.add_widget(self.label)
        self.box.add_widget(self.pars_btn)
        self.box.add_widget(self.post_btn)     
        return self.box   

    def pars_and_set_text(self):
        # print(self)
        Func.pars(self)
        print(123)
        # time.sleep(10)
        self.label.text = Func.read_file(self)


class Func():
    def pars(self):
        print('func...')
        obj = Pars()
        obj.pars_it()


    def read_file(self):
        with open(f'{PATH}/tmp/PostText.txt', "r") as f:
            text = f.read()
            # print(f'text: {text}')
            return text
    
    def post(self, text):
        # print(text)
        from bot import Bot_poster

        bot_abarmot = Bot_poster()
        bot_abarmot.post_to_tg(text)
        # print('bot post message here')




if __name__ == '__main__':
	MyApp().run()		
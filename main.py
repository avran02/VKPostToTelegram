from pars import Pars
from config import PATH, TG_CHAT_ID
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import escape_markup
from bot import Bot_poster


Builder.load_file('styles.kv')


class MyButton(Button):
    pass


Window.size = (800, 600)
Window.clearcolor = (3/255, 53/255, 78/255, 1)


class MyPopup(Popup):
    def __init__(self, message):
        super().__init__()
        self.ntf_box = BoxLayout(orientation='horizontal')
        self.buttons = list()
        self.put_button_to_notify('Опубликовать без фото')        
        self.put_button_to_notify('Закрыть')
        self.popup = Popup(title=message,
                           title_size='20sp', 
                           content=self.ntf_box, 
                           size_hint=(None, None), 
                           size=(400, 200), 
                           auto_dismiss=True,
                           title_color=(104/255, 199/255, 246/255, 1))
        self.popup.title_align = 'center'  
        self.popup.open()
    
    def put_button_to_notify(self, text):
        ntf_btn = MyButton(text = text, size_hint=(0.5, 0.4))
        self.ntf_box.add_widget(ntf_btn)
        self.buttons.append(ntf_btn)


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.pars_btn = MyButton(text = 'Спарсить последнюю НЕЗАКРЕПЛЕННУЮ запись', background_normal='')
        self.label = TextInput(text = 'Здесь будет ваш текст', size_hint=(1, 3.5))
        self.post_btn = MyButton(text = 'Запостить в телеграм')
        self.pars_pinned_btn = MyButton(text = 'Спарсить последнюю запись', background_normal='')
        self.clear_btn = MyButton(text='Очистить tmp', size_hint=(1, 0.2))
                                
    def build(self):
        self.title = 'VK post to Telegram'
        self.box = BoxLayout(orientation = 'vertical', spacing = 5)
        self.btns_box = BoxLayout(orientation='horizontal')
        self.pars_btn.bind(on_press = lambda x : self.pars_and_set_text())
        self.post_btn.bind(on_press = lambda x: Func.post(self, self.label.text))
        self.pars_pinned_btn.bind(on_press = lambda x : self.pars_pinned_and_set_text())
        self.clear_btn.bind(on_press = lambda x : Bot_poster().clear_folder())
        self.btns_box.add_widget(self.pars_btn)
        self.btns_box.add_widget(self.post_btn)  
        self.btns_box.add_widget(self.pars_pinned_btn)
        self.box.add_widget(self.label)
        self.box.add_widget(self.btns_box)
        self.box.add_widget(self.clear_btn)
        return self.box   

    def pars_and_set_text(self):
        text = Func.pars(self)
        own_text = Func.read_file(self, 'PostText')
        fw_text = Func.read_file(self, 'FwPostText')
        self.label.text = escape_markup(f'\nСобственный текст:\n\n'
                           f'{own_text}\n'
                           f'\nТекст пересланного сообщения:\n\n'
                           f'{fw_text}')

    def pars_pinned_and_set_text(self):
        text = Func.pars_pinned(self)
        own_text = Func.read_file(self, 'PostText')
        fw_text = Func.read_file(self, 'FwPostText')
        self.label.text = escape_markup(f'\nСобственный текст:\n\n'
                           f'{own_text}\n'
                           f'\nТекст пересланного сообщения:\n\n'
                           f'{fw_text}')    


class Func():
    def pars(self):
        obj = Pars()
        obj.pars_it()
    
    def pars_pinned(self):
        obj = Pars()
        obj.pars_pinned_text()

    def read_file(self, name):
        with open(f'{PATH}/tmp/{name}.txt', "r", encoding='utf-8') as f:
            text = f.read()
            return text
    
    def post(self, text):
        bot_abarmot = Bot_poster()
        resp = bot_abarmot.post_to_tg(text)
        if not resp:
            ntf = MyPopup('Фото не найдены. \nХотите выложить без них?')
            ntf.buttons[0].bind(on_press = lambda x : (bot_abarmot.bot.send_message(TG_CHAT_ID, text), ntf.popup.dismiss()))
            ntf.buttons[1].bind(on_press = lambda x : ntf.popup.dismiss())

if __name__ == '__main__':
	MyApp().run()		

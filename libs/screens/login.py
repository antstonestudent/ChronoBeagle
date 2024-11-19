from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

class Login(Screen):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "BlueGray"
        return Builder.load_file('login.kv')
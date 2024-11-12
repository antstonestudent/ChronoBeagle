# Main application base

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    pass

class TimerScreen(Screen):
    pass

class TaskEditScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AddAppScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class ChronoBeagle(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='Task Scheduler'))
        sm.add_widget(TimerScreen(name='Timer'))
        sm.add_widget(TaskEditScreen(name='Task Editor'))
        sm.add_widget(SettingsScreen(name='Settings'))
        sm.add_widget(AddAppScreen(name='Add Application'))
        sm.add_widget(LoginScreen(name='Login'))
        sm.add_widget(RegisterScreen(name='Register an Account'))
        return sm

if __name__ == '__main__':
    ChronoBeagle().run()

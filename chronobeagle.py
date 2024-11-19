# Main application base

import kivy
kivy.require('2.3.0')

import sys
import os
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.metrics import Metrics
from kivy.resources import resource_add_path

# KivyMD import classes
from kivymd.app import MDApp
from kivymd.uix.navigationbar import MDNavigationBar

# Path to the screens folder which include other screens
sys.path.append('ChronoBeagle Project/libs')
sys.path.append('ChronoBeagle Project/assets')

# Import the screens
from libs.screens.tasksched import TaskSched
from libs.screens.addapp import AddApp
from libs.screens.login import Login
from libs.screens.register import Register
from libs.screens.settings0 import Settings0
from libs.screens.taskedit import TaskEdit
from libs.screens.timer import Timer

sm = ScreenManager() # Create the ScreenManager

class ChronoBeagleApp(MDApp):
    def build(self):
        Window.size = [480, 800] # Adjust width and height if needed

        # Add screens to the ScreenManager
        sm.add_widget(TaskSched(name='tasksched'))
        # sm.add_widget(AddApp(name='addapp'))
        # sm.add_widget(Login(name='login'))
        # sm.add_widget(Register(name='register'))
        # sm.add_widget(Settings0(name='settings0'))        
        # sm.add_widget(TaskEdit(name='taskedit'))
        # sm.add_widget(Timer(name='timer'))
        # Add more screens as needed    

        return sm

if __name__ == '__main__':
    import dep_manager
    ChronoBeagleApp().run()
# Main application base

import kivy
kivy.require('2.3.0')

import subprocess
import importlib
from kivy.uix.settings import text_type
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Function to check if dependencies need to be installed from requirements.txt
def check_dependency(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

# List of required dependencies
required_dependencies = ['kivy', 'Cython', 'Pillow', 'Pygments', 'docutils', 'pygame', 'watchdog', 'numpy', 'requests' 'Pyjnius', 'Setuptools', 'PySDL2']

# Function to install dependences from requirements.txt
def install_dependencies():
    try:
        with open('requirements.txt') as f:
            for line in f:
                subprocess.check_call(['pip', 'install', '--no-cache-dir', line.strip()])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing dependencies:", e)

# Check if all required dependencies are installed
if all(check_dependency(dep) for dep in required_dependencies):
    print("All required dependencies are already installed. Skipping dependency installation.")
else:
    print("Some dependencies are missing. Proceeding with dependency installation.")
    install_dependencies() # Call the function to install dependencies

# Screenmanager pages
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
        sm.add_widget(MainScreen(name='scheduler'))
        sm.add_widget(TimerScreen(name='timer'))
        sm.add_widget(TaskEditScreen(name='taskedit'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AddAppScreen(name='addapp'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))

        # Load the .kv file using builder
        Builder.load_file('chronobeagle.kv')

        return sm

if __name__ == '__main__':
    install_dependencies()
    ChronoBeagle().run()

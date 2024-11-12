# Main application base

import kivy

import subprocess
import importlib
from kivy.uix.settings import text_type
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

# Function to check if dependencies need to be installed from requirements.txt
def check_dependency(package_name):
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

# List of required dependencies
required_dependencies = ['kivy', 'Cython', 'Pillow', 'Pygments', 'docutils', 'pygame', 'watchdog', 'numpy', 'requests']

# Function to install dependences from requirements.txt
def install_dependencies():
    try:
        with open('requirements.txt') as f:
            for line in f:
                subprocess.check_call(['pip', 'install', line.strip()])
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
        sm.add_widget(MainScreen(name='Task Scheduler'))
        sm.add_widget(TimerScreen(name='Timer'))
        sm.add_widget(TaskEditScreen(name='Task Editor'))
        sm.add_widget(SettingsScreen(name='Settings'))
        sm.add_widget(AddAppScreen(name='Add Application'))
        sm.add_widget(LoginScreen(name='Login'))
        sm.add_widget(RegisterScreen(name='Register an Account'))
        return sm

if __name__ == '__main__':
    install_dependencies()
    ChronoBeagle().run()

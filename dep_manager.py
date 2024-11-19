import subprocess
import importlib
import sys

# Redirect output to a log file
sys.stdout = open("dep_check.log", "w")

# Function to check if a dependency is installed
def check_dependency(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is installed.")
        return True
    except ImportError:
        print(f"{package_name} is missing. Installing...")
        return False

# Function to install dependencies from requirements.txt
def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', '--no-cache-dir', '-r', 'requirements.txt'])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error installing dependencies:", e)

# Function to check and install dependencies if needed
def check_and_install_dependencies(required_dependencies):
    if all(check_dependency(dep) for dep in required_dependencies):
        print("All required dependencies are already installed. Skipping dependency installation.")
    else:
        print("Some dependencies are missing. Proceeding with dependency installation.")
        install_dependencies()

# List of required dependencies
required_dependencies = ['kivy', 'Cython', 'Pillow', 'Pygments', 'docutils', 'pygame', 'watchdog', 'numpy', 'requests', 'Pyjnius', 'Setuptools', 'PySDL2']

if __name__ == '__main__':
    check_and_install_dependencies(required_dependencies)
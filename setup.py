from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
    
    requirements = [modules.replace('\n','') for modules in requirements]

    if "-e ." in requirements:
        requirements.remove("-e .")

setup(
    name = "Diamond_Price_Prediction",
    author = 'Shubhankar Chaturvedi',
    author_email = 'shubhankar58448@gmail.com',
    packages = find_packages(),
    install_require = get_requirements('requirements.txt')
)


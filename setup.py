from setuptools import find_packages, setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list

    setup(name='Insurance',
      version='0.0.1',
      description='Industry insurance pridiction',
      author='Ankur Kumar',
      author_email ='ankurscs@gmail.com',
      packages = find_packages(),
      install_requires = get_requirements()
     )
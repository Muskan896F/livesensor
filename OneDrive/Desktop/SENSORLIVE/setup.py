from setuptools import find_packages, setup
#from typing import List
#from typing import List

def get_requirements()->list[str]:
    get_requirements = list[str] =[]
    return get_requirements




setup(
name='Sensor',
version="0.0.1",
author="Muskan",
author_email="muskan17ara@gmail.com",
packages=find_packages(),
    install_requires = get_requirements(), #["pymongo"]
    
)
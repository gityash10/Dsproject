from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]


        if ('-e .' in requirements):
            requirements.remove('-e .')

    return requirements

    


setup(
    name='Dsproject',          
    version='0.0.1',
    author='Yash',
    author_email='sj9399037128@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
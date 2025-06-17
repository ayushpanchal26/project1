from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e"
def get_req(file_path :str) ->List[str]:
    '''
    This function will return the list of requirenmets.
    '''
    requirenments = []
    with open(file_path) as file_obj:
        requirenments = file_obj.readline()
        requirenments = [req.replace("\n","") for req in requirenments]

        if HYPEN_E_DOT in requirenments:
            requirenments.remove(HYPEN_E_DOT)
        
    return requirenments
setup(
name='mlporject',
version='0.0.1',
author='ayush',
author_email='ayushpanchal2605@gmail.com',
packages=find_packages(),
install_requires=get_req('requirements.txt')


)
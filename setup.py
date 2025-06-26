"""
This setup.py will be responsible for creating my machine learning application as a package. 
✅ What setup.py will do for your ML application:
Defines your app as a package — so others (or future you) can pip install it easily.
Includes metadata — name, version, author, description, license, etc.
Specifies dependencies — like scikit-learn, pandas, flask, etc.
Packages code automatically using find_packages().
Can include scripts/entry points — useful for launching your app (e.g., starting a training pipeline or web server).
Enables distribution via PyPI or internal sharing (e.g., via wheel or source tarball).
"""

from setuptools import find_packages,setup
## setup : This is the main function from setuptools used to configure your Python package.It tells Python how to build, install, and distribute your project.
## find_packages() automatically searches for all Python packages (i.e., directories that contain an __init__.py file) in your project folder, and returns a list of them to include in your distribution.
# So, If you want a folder to be included as a Python package (i.e., detected by find_packages() and included in your distribution), then:
#🔸 It must contain an __init__.py file — even if it's empty...
from typing import List



HYPEN_E_DOT = '-e.'

## Function to return the list of requirements...(-e.) shouldn't be here...
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        for line in file:
            req = line.strip()
            if req and req != HYPEN_E_DOT:
                requirements.append(req)
    return requirements

setup(
    name="Project2",
    version='0.0.1',
    author="Aniket Sinha",
    author_email="sinhaaniket010@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
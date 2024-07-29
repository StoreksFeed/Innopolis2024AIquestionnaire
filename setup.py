from setuptools import setup, find_packages

setup(
    name='Innopolis2024AIquestionnaire',
    version='0.1.0',
    description='A library providing tools for psychological AI evaluation',
    author='Semyon Glazyrin',
    url='https://github.com/StoreksFeed/Innopolis2024AIquestionnaire',
    packages=find_packages(),
    install_requires=[
        'contourpy==1.2.1',
        'cycler==0.12.1',
        'fonttools==4.53.1',
        'kiwisolver==1.4.5',
        'matplotlib==3.9.1',
        'numpy==2.0.1',
        'packaging==24.1',
        'pillow==10.4.0',
        'pyparsing==3.1.2',
        'python-dateutil==2.9.0.post0',
        'six==1.16.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.11'
)

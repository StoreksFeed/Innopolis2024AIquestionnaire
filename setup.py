from setuptools import setup, find_packages

setup(
    name='Innopolis2024AIquestionnaire',
    version='2.0.0',
    description='A library providing tools for psychological AI evaluation',
    author='Semyon Glazyrin, Dmitry Samokhvalov',
    url='https://github.com/StoreksFeed/Innopolis2024AIquestionnaire',
    packages=find_packages(),
    install_requires=[
        'certifi==2024.7.4',
        'charset-normalizer==3.3.2',
        'contourpy==1.2.1',
        'cycler==0.12.1',
        'fonttools==4.53.1',
        'idna==3.7',
        'kiwisolver==1.4.5',
        'matplotlib==3.9.1',
        'numpy==2.0.1',
        'packaging==24.1',
        'pillow==10.4.0',
        'pyparsing==3.1.2',
        'python-dateutil==2.9.0.post0',
        'requests==2.32.3',
        'six==1.16.0',
        'urllib3==2.2.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.11',
    package_data={
        'Innopolis2024AIquestionnaire': ['data/*']
    }
)

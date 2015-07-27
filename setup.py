from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Wordcount sample project',
    version='1.0.0',
    description='Wordcount sample project',
    author='Shastinathan Sivasubramanian',
    author_email='shastinathan.s@gmail.com',
    test_suite='',
    install_requires=required,
    url=''
)

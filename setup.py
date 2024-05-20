from setuptools import setup, find_packages

setup(
    name='Lamedh',
    version='0.1',
    url='https://github.com/lamedh.git',
    author='Javier Mansilla',
    author_email='javimansilla@gmail.com',
    description='Lambda Reduction and Evaluation',
    packages=find_packages(),
    scripts=['bin/lamedh'],
    install_requires=['parsimonious>=0.10'],
)

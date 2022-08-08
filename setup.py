from setuptools import setup, find_packages

setup(
    name='Minesweeper',
    packages=find_packages(include=['Minesweeper', 'Minesweeper.utils', 'Minesweeper.exceptions']),
    version='0.1.0 beta',
    description='A Library to make minesweeper games easily using OOP',
    author='Ousama Alhennawi',
    license='MIT'
)
from setuptools import setup
from awsgoes16 import __version__

setup(
    name='awsgoes16',
    version=__version__,
    packages=['awsgoes16'],
    entry_points={
        'console_scripts': [
            'awsgoes16 = awsgoes16.main:main'
        ]
    })

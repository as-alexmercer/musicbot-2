
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='musicbot',
    version='0.6.0',
    description='Music swiss army knife',
    python_requires='<3.9,>=3.8',
    author='Adrien Pensart',
    author_email='crunchengine@gmail.com',
    license='MIT',
    entry_points={"console_scripts": ["musicbot = musicbot.cli:main"]},
    packages=['musicbot', 'musicbot.commands', 'musicbot.music'],
    package_dir={"": "."},
    package_data={"musicbot": ["schema/*.sql"]},
    install_requires=['attrdict==2.*,>=2.0.0', 'attrs==20.*,>=20.1.0', 'click-skeleton==0.*,>=0.3.3', 'colorlog==4.*,>=4.1.0', 'enlighten==1.*,>=1.6.1', 'graphql-py==0.*,>=0.7.1', 'humanfriendly==8.*,>=8.1.0', 'jellyfish==0.*,>=0.8.2', 'logging-tree==1.*,>=1.8.0', 'mutagen==1.*,>=1.44.0', 'prettytable==0.*,>=0.7.2', 'prompt-toolkit==3.*,>=3.0.2', 'pyacoustid==1.*,>=1.1.0', 'pydub==0.*,>=0.24.0', 'pyrsistent==0.17.2', 'python-slugify==4.*,>=4.0.0', 'python-vlc==3.*,>=3.0.0', 'requests==2.*,>=2.24.0', 'spotipy==2.*,>=2.10.0', 'watchdog==0.*,>=0.10.0', 'youtube-dl==2020.*,>=2020.1.24'],
    extras_require={"dev": ["bump2version==1.*,>=1.0.0", "coverage-badge==1.*,>=1.0.0", "dephell==0.*,>=0.8.3", "html5lib==1.*,>=1.0.1", "mypy==0.*,>=0.782.0", "pygments==2.*,>=2.7.0", "pylint==2.*,>=2.6.0", "pytest-cov==2.*,>=2.6.0", "pytest-docker-compose==3.*,>=3.1.2", "pytype==2020.*,>=2020.8.28", "restructuredtext-lint==1.*,>=1.3.0"]},
)

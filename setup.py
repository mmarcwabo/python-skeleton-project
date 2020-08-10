try:
    from setuptools import setup

except:
    from distutils.core import setup

config =  {
    'description' : 'Manage courses',
    'author': 'mwabo',
    'url': 'https://projects.exsofth.com/mcdemo/',
    'author_url': 'https://projects.exsofth.com/mcdwn/',
    'author_email': 'mwabo@exsofth.com',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages':['app'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
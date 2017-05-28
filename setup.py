from setuptools import setup

setup(
    name = 'hello',
    version = '0.1.0',
    description = 'dummpy application used in recipes',
    url = 'https://github.com/buildbot-cookbook/hello',
    packages = ['hello',],
    entry_points = {
        'console_scripts': [
            'hello = hello.hello:main',
        ],
    },
    license = 'GPL V3',
    author = 'David Froger',
    author_email = 'david.froger@mailoo.org',
)

from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = 'Amino.py',
    version = '1.0.3',
    url = 'https://github.com/Slimakoi/Amino.py',
    download_url = 'https://github.com/Slimakoi/Amino.py/tarball/master',
    license = 'GPLv3',
    author = 'Slimakoi',
    author_email = 'slimeytoficial@gmail.com',
    description = 'Unofficial python wrapper for the Amino web api',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = [
        'aminoapps',
        'amino-py',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'slimakoi'
        'unofficial'
    ],
    install_requires = [
        'setuptools',
        'requests',
        'six',
        'websocket-client',
        'ffmpeg-python'
    ],
    setup_requires = [
        'wheel'
    ],
    packages = find_packages()
)

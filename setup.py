from setuptools import setup

setup(
    name='snapshotalyzer-30K',
    version='0.1',
    author="Krishna Vinay",
    author_email="vinaysm1@gmail.com",
    description="snapshotalyzer-3K is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/vinaysm1/Snapshotalyzer-30K",
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)

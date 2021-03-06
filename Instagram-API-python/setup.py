from setuptools import setup

setup(
    name='InstagramAPI',
    version='1.0.2',
    description='Unofficial instagram API, give you access to ALL instagram features (like, follow, upload photo and video and etc)! Write on python.',
    url='https://github.com/aashishdugar/Instagram-API-python/',
    author='aashish dugar',
    author_email='aashish_d@live.com',
    license='GNU',
    packages=['InstagramAPI'],
    zip_safe=False,
    install_requires=[
        "requests==2.11.1",
        "requests-toolbelt==0.7.0",
        "moviepy==0.2.3.2"
    ])

from setuptools import setup, find_packages

import piehunter as app

setup(
    name="django-piehunter",
    version=app.__version__,
    description="Automatic Tastypie URL builder by way of import discovery.",
    author="Zenobius Jiricek",
    author_email="airtonix@gmail.com",
    url="http://github.com/airtonix/django-piehunter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-tastypie',
    ],
)
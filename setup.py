#coding:utf-8

from distutils.core import setup
from setuptools import find_packages


PACKAGE = "news_api"
NAME = "news_api"
DESCRIPTION = "API of news in China."
AUTHOR = "UlionTse"
AUTHOR_EMAIL = "shinalone@outlook.com"
URL = "https://github.com/shinalone/news_api"
VERSION = __import__(PACKAGE).__version__

with open('README.rst','r',encoding='utf-8') as file:
    long_description = file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords=['news_api','News','news','NewsApi','newsAPI'],
    install_requires=[
        'pymysql>=0.8.0',
        'requests>=2.18.4',
        'jieba>=0.39',
        'snownlp>=0.12.3',
        'beautifulsoup4>=4.6.0',
        'true_encoding>=1.0.2'
    ],
    zip_safe=False,
)


# class Config:
#     SECRET_KEY = 'your_secret_key_here'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///news.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     NEWS_API_KEY = '3555940ae6544172984c581617e5235e'  # NewsAPIのAPIキー

# # config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///news.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    API_KEY = os.environ.get('NEWAPI_KEY', '3555940ae6544172984c581617e5235e')

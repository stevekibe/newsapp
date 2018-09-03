import os
class Config:
    '''
    general config class
    '''
    SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORY_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}&country=us&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY =os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):

    pass

class Devconfig(Config):

    DEBUG = True

Config_options = {
    'development':Devconfig,
    'production': ProdConfig
}

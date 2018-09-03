import urllib.request,json
from .models import News, Source, Category


#getting api key

api_key = None 

#Getting the news base url

base_url = None
news_url = None
category_url = None

def configure_request(app):
    global api_key, base_url, news_url, category_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    news_url = app.config['NEWS_API_BASE_URL']
    category_url = app.config['CATEGORY_API_BASE_URL']
def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_sources = None

        if get_sources_response['sources']:
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)
                
    return news_sources

def process_sources(sources_list):
    
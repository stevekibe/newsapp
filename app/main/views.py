from flask import render_template
from . import main
from ..request import get_sources, get_news, get_category


@main.route('/')
def index():
    '''
    method to route the main newws in the app
    '''
    # having the new category
    general_news = get_sources( 'general' )
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    health_news = get_sources('health')
    technology_news = get_sources('technology')
    sports_news = get_sources('sports')

    title = "Time-News"
    return render_template('index.html', title=title, general = general_news,
    business = business_news, entertainment = entertainment_news, health = health_news, technology = technology_news, sports = sports_news)

@main.route('/news/<id>')
def news(id):
    '''
    method to ruote the news
    '''
    news_articles = get_news(id)
       
    return render_template('general.html', general = news_articles)
    '''
    main route to get the news 
    '''
    

@main.route('/categories/<category>')
def general(category):
    '''
    method to route the news catergory
    '''
    news_categories_articles = get_category(category)

    return render_template('news.html', news = news_categories_articles)


@main.route('/categories/<category>')
def sports(category):
    '''
    method to route the sports category
    '''
    news_categories_articles = get_category(category)

    return render_template('sports.html', sports = news_categories_articles)


@main.route('/categories/<category>')
def health(category):
    '''
    method to ruote the health category
    '''
    news_categories_articles = get_category(category)

    return render_template('health.html', health=news_categories_articles)


@main.route('/categories/<category>')
def technology(category):
    '''
    method to route the technolgy category
    '''
    news_categories_articles = get_category(category)

    return render_template('technology.html', technology = news_categories_articles)
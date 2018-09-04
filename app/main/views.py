from flask import render_template
from . import main
from ..request import get_sources, get_news, get_category


@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
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
def general(id):
    '''
    view root page function that returns the news page and its data
    '''
    news_articles = get_news(id)
       
    return render_template('general.html', general = news_articles)
    '''
    main route to get the news 
    '''
    

@main.route('/categories/<category>')
def news(category):
    '''
    view page function that returns the categories page and its data
    '''
    news_categories_articles = get_category(category)

    return render_template('news.html', news = news_categories_articles)


@main.route('/categories/<category>')
def sports(category):
    '''
    view page function that returns the categories page and its data
    '''
    news_categories_articles = get_category(category)

    return render_template('sports.html', sports = news_categories_articles)


@main.route('/categories/<category>')
def health(category):
    '''
    view  page function that returns the categories page and its data
    '''
    news_categories_articles = get_category(category)

    return render_template('health.html', health=news_categories_articles)


@main.route('/categories/<category>')
def technology(category):
    '''
    view root page function that returns the categories page and its data
    '''
    news_categories_articles = get_category(category)

    return render_template('technology.html', technology = news_categories_articles)
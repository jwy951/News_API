from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles,search_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting sources by category
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    health_sources = get_sources('health')
    science_sources = get_sources('science')

    title = 'Home - Welcome to The best News Website Online'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('main.search',article_name = search_article))
    else:
        return render_template('index.html', title = title, general = general_sources, business = business_sources, technology = technology_sources, sports = sports_sources, entertainment = entertainment_sources, health = health_sources, science = science_sources)
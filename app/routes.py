# app/routes.py

from flask import Blueprint, render_template, request, current_app
import requests
from app import db
from app.models import Article

main = Blueprint('main', __name__)

@main.route('/')
def index():
    country = request.args.get('country', 'jp')
    api_key = current_app.config['API_KEY']
    base_url = 'https://newsapi.org/v2/top-headlines'

    response = requests.get(base_url, params={'country': country, 'apiKey': api_key})
    articles = response.json().get('articles', [])

    # Save articles to the database
    for article in articles:
        if not Article.query.filter_by(url=article['url']).first():
            new_article = Article(
                title=article['title'],
                url=article['url'],
                published_at=article['publishedAt']
            )
            db.session.add(new_article)
    db.session.commit()

    # Fetch articles from the database
    saved_articles = Article.query.all()
    return render_template('index.html', articles=saved_articles)

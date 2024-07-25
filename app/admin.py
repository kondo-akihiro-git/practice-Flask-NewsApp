# app/admin.py

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, request

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

class ArticleModelView(SecureModelView):
    column_list = ('title', 'url', 'published_at')
    form_columns = ('title', 'url', 'published_at')

def setup_admin(app):
    from app import db
    from app.models import Article

    admin = Admin(app, name='News Admin', template_mode='bootstrap3')
    admin.add_view(ArticleModelView(Article, db.session))
